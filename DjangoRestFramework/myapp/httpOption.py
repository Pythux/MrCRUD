
from rest_framework.metadata import SimpleMetadata


class AllowMetadata(SimpleMetadata):
    """json returned for OPTIONS methode:"""
    def determine_metadata(self, request, view):
        to_return = super().determine_metadata(request, view)
        return to_return
