"""Views positions"""
from department_app.rest.serializers import PositionsListSerializer
from department_app.models import Positions
from rest_framework import viewsets


class PositionsViewSet(viewsets.ModelViewSet):
    """"Create, read, update, delete"""
    queryset = Positions.objects.all()
    serializer_class = PositionsListSerializer


# class PositionsHome(ListView):
#     model = Positions
#     template_name = 'positions.html'
#     context_object_name = 'positions'
#
#
# # def index_positions(request):
# #     positions = Positions.objects.all()
# #     context = {
# #         'positions': positions,
# #     }
# #     return render(request, 'positions.html', context=context)
#
# class EditPositions(UpdateView):
#     model = Positions
#     fields = ['name']
#     template_name = 'edit_positions.html'
#     pk_url_kwarg = 'positions_id'
#     context_object_name = 'positions'
#     success_url = reverse_lazy('positions')
#
#
# # def edit_positions(request, positions_id):
# #     positions = Positions.objects.filter(pk=positions_id)
# #     # context = {
# #     #     'positions': positions,
# #     # }
# #     if request.method == "POST":
# #         positions.name = request.POST.get("name").save()
# #         return HttpResponseRedirect("/positions/")
# #     else:
# #         return render(request, 'edit_positions.html', context={'positions': positions})
#
#
# class AddPositions(CreateView):
#     model = Positions
#     fields = ['name']
#     template_name = 'add_positions.html'
#     context_object_name = 'positions'
#     success_url = reverse_lazy('positions')
#
#
# # def add_positions(request):
# #     if request.method == 'POST':
# #         form = AddPositionsForm(request.POST)
# #         if form.is_valid():
# #             # print(form.cleaned_data)
# #             form.save()
# #             # Positions.objects.create(**form.cleaned_data)
# #             return redirect('positions')
# #     else:
# #         form = AddPositionsForm()
# #     return render(request, "add_positions.html", {'form': form})
#
#
# def delete(request, positions_id):
#     Positions.objects.get(id=positions_id).delete()
#     return HttpResponseRedirect("/positions/")
