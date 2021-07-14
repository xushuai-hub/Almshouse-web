from rest_framework.filters import SearchFilter


class OldSearchFilter(SearchFilter):
    search_param = 'username'

    def get_search_fields(self, view, request):
        return ['ID', 'username', 'gender', 'phone',
                'birthday', 'checkin_date', 'checkout_date',
                'room_number', 'health_state']


class VolunteerSearchFilter(SearchFilter):
    search_param = 'username'

    def get_search_fields(self, view, request):
        return ['id', 'username', 'gender', 'phone', 'id_card',
                'birthday', 'checkin_date', 'checkout_date']


class EmployeeSearchFilter(SearchFilter):
    search_param = 'username'

    def get_search_fields(self, view, request):
        return ['id', 'username', 'gender', 'phone', 'id_card',
                'birthday', 'hire_date', 'resign_date']
