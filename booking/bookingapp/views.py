from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from .forms import BookingForm

# Home view
def home(request):
    return render(request, "index.html")

# Booking view
def book(request):
    return render(request, "book.html")

# View to list all bookings
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'bookingapp/booking_list.html', {'bookings': bookings})

# Booking detail view for create and update
def booking_detail(request, id=None):
    if id:
        booking = get_object_or_404(Booking, id=id)
    else:
        booking = None

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'bookingapp/details.html', {'form': form})

# Delete booking view
def delete_booking(request, id):
    booking = get_object_or_404(Booking, id=id)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    
    return render(request, 'bookingapp/delete_booking.html', {'booking': booking})
