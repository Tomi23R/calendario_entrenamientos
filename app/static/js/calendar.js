// Get number of days in a month
var getDaysInMonth = function(month,year) {
    // Here January is 1 based
    //Day 0 is the last day in the previous month
   return new Date(year, month, 0).getDate();
  // Here January is 0 based
  // return new Date(year, month+1, 0).getDate();
};

function fillCalendar(id, day, month, year){
    cells = document.querySelectorAll('#' + id + ' td');
    var n_days = getDaysInMonth(month, year);
    var first_day = new Date(year, month, 1);
    var day_week = first_day.getDay();
    var count = 0;
    // Si el primer dia del mes es domingo empezamos a rellenar en la posicion 6
    if(day_week == 0){
        var start = 6;
    }
    else{
        start = day_week - 1;
    }

    // Rellenamos la tabla con los dias de la semana
    for(i = count; i < n_days; i++){
        cells[i].innerText = count + 1;
        if(count + 1 == day){
            cells[i].className += "table-active";
        }
        count++;
    }
}

// Funcion de carga de la pagina
$(document).ready(function() {
    var meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
                'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    var today = new Date();
    document.getElementById("month").innerText = meses[today.getMonth()];
    fillCalendar("calendar-body", today.getDate(), today.getMonth(), today.getFullYear());
})




