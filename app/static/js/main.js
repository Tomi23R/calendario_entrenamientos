// Get number of days in a month
var getDaysInMonth = function(month,year) {
  // Here January is 0 based
  return new Date(year, month+1, 0).getDate();
};

// Fill calendar with specific month
function fillCalendar(day, month, year){
    var meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
                'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
    cells = $('.celda');
    var n_days = getDaysInMonth(month, year);
    var first_day = new Date(year, month, 1);
    var day_week = first_day.getDay();
    var count = 1;
    // Si el primer dia del mes es domingo empezamos a rellenar en la posicion 6
    if(day_week == 0){
        var start = 6;
    }
    else{
        var start = day_week - 1;
    }

    // Rellenamos la tabla con los dias de la semana
    for(i = start; i < n_days + start; i++){
        fecha = count + '-' + (month + 1) + '-' + year
        contenido = 
            "<div class='row dia-container'>" +
                "<div class='col text-left dia'>" + count + "</div>"+
            "</div>"+
            "<div class='row'>"+
                "<div class='col contenido-celda'></div>"+
            "</div>"+
            "<div class='row'>"+
                "<div class='col anadir-container'><button data-date='" + fecha + "' class='btn btn-outline-light anadir-entrenamiento' data-bs-toggle='modal' data-bs-target='#createTraining'>+</button></div>"+
            "</div>";
        cells[i].innerHTML = contenido;
        count++;
    }

    // Limpiamos las celdas que no tienen contenido
    for(i = 0; i < start; i++){
        cells[i].classList.add('not_active');
    }
    for(i = n_days + start; i < cells.length; i++){
        cells[i].classList.add('not_active');
    }

    // Setteamos el mes
    document.getElementById("month").innerText = meses[month] + " - " + year;
}

function clean_calendar(){
    $('.celda div').remove();
    $('.celda').removeClass('not_active');
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

// Funcion que settea los botnes de next y back del modal
function prep_modal()
{
    $(".modal").each(function() {
        var element = this;
        var pages = $(this).find('.modal-split');
        if (pages.length != 0){
            pages.hide();
            pages.eq(0).show();
            var b_button = document.createElement("button");
                b_button.setAttribute("type","button");
                b_button.setAttribute("class","btn btn-primary");
                b_button.setAttribute("style","display: none;");
                b_button.innerHTML = "Atras";
            
            var n_button = document.createElement("button");
                n_button.setAttribute("type","button");
                n_button.setAttribute("class","btn btn-primary");
                n_button.innerHTML = "Siguiente";
            
            $(this).find('.modal-footer').append(b_button).append(n_button);
            var page_track = 0;
            $(n_button).click(function() {
                this.blur();
                if(page_track == 0){
                    $(b_button).show();
                }
                if(page_track == pages.length-2){
                    $(n_button).text("Crear entrenamiento");
                }
                if(page_track == pages.length-1){
                    $(element).find("form").submit();
                }
                if(page_track < pages.length-1){
                    page_track++;
                    pages.hide();
                    pages.eq(page_track).show();
                }
            });
            $(b_button).click(function() {
                if(page_track == 1){
                    $(b_button).hide();
                }
                if(page_track == pages.length-1){
                    $(n_button).text("Next");
                }
                if(page_track > 0){
                    page_track--;
                    pages.hide();
                    pages.eq(page_track).show();
                }
            });
        }
    });
}

// Funcion para cargar las acciones del modal de crear entrenamiento de running
function load_running(){
    $('.anadir-entrenamiento').on('click', function() {
        $('#training_date').val($(this).data('date'));
    });

    // Selector del tipo de entrenamiento
    $('#training_type').change(function(){
        $('#rodaje').css('display', 'none');
        $('#bloques').css('display', 'none');
        $('#entrenamiento_bloques').css('display', 'none');

        var selected_option = $(this).val();
        // Rodaje por tiempo
        if(selected_option == 1){
            $('#rodaje').css('display', 'block');
            $('#rodaje1').text('Tiempo:');
        }
        // Rodaje por distancia
        else if(selected_option == 2){
            $('#rodaje').css('display', 'block');
            $('#rodaje1').text('Distancia:');
        }
        // Series por tiempo
        else if(selected_option == 3){
            $('#bloques').css('display', 'block');
            $('#bloques_3').text('Tiempo');
        }
        // Series por distancia
        else if(selected_option == 4){
            $('#bloques').css('display', 'block');
            $('#bloques_3').text('Distancia');
        }
        // Otro
        else{
            $('#entrenamiento_bloques').css('display', 'block');
        }
    });

    // Radio button para seleccionar tipo de entrenamiento otro
    $('#entrenamiento_bloques input:radio').on('change', function(){
        $('#bloques').css('display', 'none');
        var value = $(this).val();
        if(value == 0){
            $('#bloques').css('display', 'block');
            $('#bloques_3').text('Distancia');
        }else if(value == 1){
            $('#bloques').css('display', 'block');
            $('#bloques_3').text('Tiempo');
        }
    })
}

// Funcion de carga de la pagina
$(document).ready(function() {
    // Acciones relacionadas con el calendario
    var today = new Date();
    fillCalendar(today.getDate(), today.getMonth(), today.getFullYear());
    $("#next_month").click(next_month);
    $("#previous_month").click(previous_month);
    prep_modal();

    // Crear entrenamiento
    load_running()
})




