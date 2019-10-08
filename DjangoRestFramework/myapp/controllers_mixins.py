
from rest_framework.exceptions import PermissionDenied


class AllowMixin:
    def _allowed_methods(self):
        methods = [m.upper() for m in self.http_method_names if hasattr(self, m)]

        original_request_method = self.request.method  # change self.request.method for each methods
        is_on_object = True
        try:
            obj = self.get_object()
        except (AssertionError, PermissionDenied):
            is_on_object = False

        for method in methods.copy():  # copy because we will delete elements of it
            self.request.method = method
            for permisson in self.get_permissions():
                if (not is_on_object and not permisson.has_permission(self.request, self)) \
                        or (is_on_object and not permisson.has_object_permission(self.request, self, obj)):
                    methods.remove(method)
                    print('remove: ' + method)
                    break

        self.request.method = original_request_method
        return methods
