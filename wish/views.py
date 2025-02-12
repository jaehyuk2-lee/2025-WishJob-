from django.shortcuts import render


# Create your views here.
def main(request):
    floor = request.GET.get("floor", "1")
    day = request.GET.get("day", "1")

    return render(
        request,
        "wish/main.html",
        {"floor": int(floor), "day": int(day)},
    )
