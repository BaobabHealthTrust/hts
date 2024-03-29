function checkFirstSecondTestAvailable() {

    var descriptions = ['First Test', 'Second Test']

    var available = {};

    for (var i = 0; i < descriptions.length; i++) {

        window.parent.stock.ajaxRequest("/stock/available_kits_by_desctiption/" + encodeURIComponent(descriptions[i]), function (data) {

            if (!data)
                var data = {};

            var json = (typeof data == typeof String() ? JSON.parse(data) : data)

            if (json.name) {

                available[json.description] = {name: json.name, present: true};

            } else {

                available[json.description] = {name: json.name, present: false};

            }


        });

    }

    window.parent.stock.availableByDescription = available;

}

function validateDescription() {

    var description = __$('touchscreenInput' + tstCurrentPage).value.trim();

    var available = window.parent.stock.availableByDescription;

    if (available[description]) {

        setTimeout(function () {

            gotoPage(tstCurrentPage - 1, false, true);

            window.parent.stock.showMsg(available[description].name + ' is already set as ' + description, "Item with description already exists");

            var ok = window.parent.stock.$("ok_button");

            ok.setAttribute("onclick", 'window.parent.stock.listItems(window.parent.document.body)');

        }, 10);

    }

}

function reloadDescriptions() {

    if(__$('touchscreenInput' + tstCurrentPage).value.match(/dts/i)) {

        if(__$("data.description")) {

            var options = __$("data.description").getElementsByTagName("option");

            for(var i = options.length - 1; i >= 0; i--) {

                var option = options[i];

                if(['First Test','Second Test'].indexOf(option.innerHTML.trim()) >= 0) {

                    __$("data.description").removeChild(options[i]);

                }

            }

        }

    } else {

        if(__$("data.description")) {

            var options = __$("data.description").getElementsByTagName("option");

            var labels = ['First Test','Second Test'];

            var options = __$("data.description").getElementsByTagName("option");

            var found = false;

            for(var i = 0; i < options.length; i++) {

                var option = options[i];

                if(labels.indexOf(option.innerHTML.trim()) >= 0) {

                    found = true;

                    break;

                }

            }

            if(!found) {

                for (var i = 0; i < labels.length; i++) {

                    var opt = document.createElement("option");
                    opt.innerHTML = labels[i];

                    __$("data.description").appendChild(opt);

                }

            }

        }

    }

}