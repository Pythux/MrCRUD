from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import get_object_or_404


class AllowMixin:
    def _allowed_methods(self):
        methods = [m.upper() for m in self.http_method_names if hasattr(self, m)]

        # check if is auth:
        try:
            self.request.auth
        except AuthenticationFailed:
            return methods

        original_request_method = self.request.method  # change self.request.method for each methods
        is_on_object = True
        try:
            obj = self._get_object_without_permissions_check()
        except AssertionError:
            is_on_object = False

        for method in methods.copy():  # copy because we will delete elements of it
            self.request.method = method
            for permisson in self.get_permissions():
                if (not permisson.has_permission(self.request, self)) \
                        or (is_on_object and not permisson.has_object_permission(self.request, self, obj)):
                    methods.remove(method)
                    break

        self.request.method = original_request_method
        return methods

    def _get_object_without_permissions_check(self):
        """no permissions check"""
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)

        self.cached_obj = obj
        return obj

    def get_object(self):
        """ Overided to retrive cached object form _get_object_without_permission_check"""
        obj = self.cached_obj
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj
