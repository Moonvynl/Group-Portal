from django.contrib import messages
from django.shortcuts import redirect


class UserIsOwnerMixin(object):
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.creator == self.request.user:
            return super().dispatch(request, *args, **kwargs)

        else:
            messages.add_message(
                request,
                messages.INFO,
                "Only owner can change it"
            )
            referring_url = request.META.get('HTTP_REFERER')
            return redirect(referring_url)
