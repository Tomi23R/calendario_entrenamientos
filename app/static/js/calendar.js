// Get number of days in a month
var getDaysInMonth = function(month,year) {
  // Here January is 0 based
  return new Date(year, month+1, 0).getDate();
};

// Fill calendar with specific month
function fillCalendar(day, month, year){
    var meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
                'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
    cells = document.querySelectorAll('#calendar-body td');
    var n_days = getDaysInMonth(month, year);
    var first_day = new Date(year, month, 1);
    var day_week = first_day.getDay();
    var count = 1;
    // Si el primer dia del mes es domingo empezamos a rellenar en la posicion 6
    if(day_week == 0){
        var start = 6;
    }
    else{
        start = day_week - 1;
    }

    // Rellenamos la tabla con los dias de la semana
    for(i = start; i < n_days + start; i++){
        cells[i].innerText = count;
        if(count == day){
            cells[i].className += "table-active";
        }
        count++;
    }
    // Setteamos el mes
    document.getElementById("month").innerText = meses[month] + " - " + year;
}

function clean_calendar(){
    cells = document.querySelectorAll('#calendar-body td');
    for(i = 0; i < cells.length; i++){
        cells[i].innerText = ''
        cells[i].className = ''
    }
}

function next_month(){
    var meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
                'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
    clean_calendar();
    var str_date = document.getElementById('month').innerText;
    var str_list = str_date.split(' - ');
    var month = meses.indexOf(str_list[0]);
    var year = parseInt(str_list[1]);
    if(month == 11){
        var var_next_month = 0;
        var var_next_year = year + 1;
    }
    else{
        var var_next_month = month + 1;
        var var_next_year = year;
    }
    fillCalendar(0, var_next_month, var_next_year);
}

function previous_month(){
    var meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
                'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
    clean_calendar();
    var str_date = document.getElementById('month').innerText;
    var str_list = str_date.split(' - ');
    var month = meses.indexOf(str_list[0]);
    var year = parseInt(str_list[1]);
    if(month == 0){
        var var_next_month = 11;
        var var_next_year = year - 1;
    }
    else{
        var var_next_month = month - 1;
        var var_next_year = year;
    }
    fillCalendar(0, var_next_month, var_next_year);
}

// Funcion de carga de la pagina
$(document).ready(function() {
    var today = new Date();
    fillCalendar(today.getDate(), today.getMonth(), today.getFullYear());
    $("#next_month").click(next_month);
    $("#previous_month").click(previous_month);
})




