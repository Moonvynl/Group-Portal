from django.core.exceptions import PermissionDenied

class CreatorIsOwnerMixin():
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.creator != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

class AuthorIsOwnerMixin():
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)