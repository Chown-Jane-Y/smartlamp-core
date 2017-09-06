# coding: utf-8
from django.db.models import Q, QuerySet
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import detail_route
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import datetime

from .models import Lamp
from .serializers import LampSerializer
from .filters import LampFilter
from utils.constants import *


class LampViewSet(viewsets.ModelViewSet):

    queryset = Lamp.objects.all().filter(is_deleted=False)
    serializer_class = LampSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filter_class = LampFilter
    ordering_fields = ('id', 'sn', 'registered_time', 'is_repeated', 'status', 'rf_band', 'channel', 'address')

    def _query(self, request, queryset=None):
        """
        Multi-condition dynamic fuzzy query.
        This method has been abandoned, because all filters are move to .filters.py. 
        """

        query_params = dict(request.query_params)
        for kw in query_params.copy():
            # If the query_param is empty, drop it.
            if not query_params[kw][0]:
                query_params.pop(kw)
        print('query_params：', query_params)

        Q_sn = Q()
        Q_start_time = Q()
        Q_end_time = Q()
        Q_others = Q()

        for kw in query_params:

            if kw == 'sn' and ',' in query_params[kw][0]:
                # sn逗号查询，如['20160805,20170911']，进行or联结
                for sn in query_params[kw][0].split(','):
                    Q_sn.add(Q(**{kw + '__icontains': sn}), Q.OR)     # icontains: case-insensitive
            elif kw == 'sn' and ',' not in query_params[kw]:
                Q_sn.add(Q(**{kw + '__icontains': query_params[kw][0]}), Q.AND)

            if kw == 'start_time':
                start_date_str = query_params[kw][0].split('T')[0]
                start_date = datetime.date(
                    int(start_date_str.split('-')[0]),
                    int(start_date_str.split('-')[1]),
                    int(start_date_str.split('-')[2]))
                end_date = datetime.date(MAX_YEAR, MAX_MONTH, MAX_DAY)
                Q_start_time.add(Q(**{'registered_time__range': (start_date, end_date)}), Q.AND)

            if kw == 'end_time':
                start_date = datetime.date(MIN_YEAR, MIN_MONTH, MIN_DAY)
                end_date_str = query_params[kw][0].split('T')[0]
                end_date = datetime.date(
                    int(end_date_str.split('-')[0]),
                    int(end_date_str.split('-')[1]),
                    int(end_date_str.split('-')[2]))
                Q_start_time.add(Q(**{'registered_time__range': (start_date, end_date)}), Q.AND)

            if kw not in ['sn', 'start_time', 'end_time']:
                Q_others.add(Q(**{kw + '__icontains': query_params[kw][0]}), Q.AND)

        if queryset is None:
            queryset = self.queryset.filter(Q_sn, Q_start_time, Q_end_time, Q_others)
        else:
            queryset = queryset.filter(Q_sn, Q_start_time, Q_end_time, Q_others)

        return queryset

    def list(self, request, *args, **kwargs):
        """
        List all lamps.
        """

        response = super(LampViewSet, self).list(self, request, *args, **kwargs)
        return response

    def destroy(self, request, *args, **kwargs):
        """
        Delete a lamp by id. 
        Set 'is_deleted' as True, and set the 'deleted_time' as time_now.
        :param request: 
        :param args: 
        :param kwargs: 
        :return: 
        """

        instance = self.get_object()
        instance.is_deleted = True
        instance.deleted_time = datetime.datetime.now()
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @detail_route(methods=['POST'], url_path='on')
    def turn_on(self, request, *args, **kwargs):
        print('turn on')
        print(request)
        # todo: 需要下发指令到硬件

        return Response({'success': True, 'msg': '亮灯'})

    @detail_route(methods=['POST'], url_path='off')
    def turn_on(self, request, *args, **kwargs):
        print('turn off')
        print(request)
        # todo: 需要下发指令到硬件

        return Response({'success': True, 'msg': '灭灯'})


class HubLampViewSet(LampViewSet):

    queryset = Lamp.objects.all().filter(is_deleted=False)
    serializer_class = LampSerializer

    def list(self, request, *args, **kwargs):
        """
        Get list of lamps by hub_sn.
        """

        hub_sn = self.kwargs['hub_sn']
        queryset = Lamp.objects.filter(hub_sn=hub_sn)
        queryset = self._query(request, queryset=queryset)

        if isinstance(queryset, QuerySet):
            queryset = queryset.all()

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
