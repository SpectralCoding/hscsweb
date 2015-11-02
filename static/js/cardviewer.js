CardViewer = {};
CardViewer.cardinfo = {};
$(document).ready(function() {
    $.getJSON( "/static/js/cards.json", function(jscardinfo) {
        CardViewer.cardinfo = {};
        var cardlist = [];
        for (var xpack in jscardinfo) {
            for (var cardid in jscardinfo[xpack]) {
                CardViewer.cardinfo[jscardinfo[xpack][cardid].id] = jscardinfo[xpack][cardid];
                cardlist[jscardinfo[xpack][cardid].name] = jscardinfo[xpack][cardid].id;
            }
        }
        var namesort = Object.keys(CardViewer.cardinfo).sort( function(keyA, keyB) {
            return CardViewer.cardinfo[keyA].name.localeCompare(CardViewer.cardinfo[keyB].name);
        });
        for (var idx in namesort) {
            $('#cardsel')
                .append($("<option></option>")
                .attr("value",namesort[idx])
                .text(CardViewer.cardinfo[namesort[idx]].name));
        }
    });
    $.getJSON( "/cardviewer/metriclist", function(metriclist) {
        metriclist.sort();
        $.each(metriclist, function(key, value) {
            $('#metricsel')
                .append($("<option></option>")
                .attr("value",key)
                .text(value));
        });
    });
    $("#viewbtn").click(function(){
        var cardname = $("#cardsel option:selected").val();
        var metricname = $("#metricsel option:selected").text();
        $.getJSON("/cardviewer/" + cardname + "/", function(carddata) {
            metricdata = carddata[metricname];
            console.log(metricdata);
            var highest = 0;
            for (var turn in metricdata) {
                if (turn > highest) {
                    highest = turn;
                }
            }
            var values = [];
            for (i = 0; i <= highest; i++) {
                if(metricdata.hasOwnProperty(i)) {
                    values.push(metricdata[i]);
                } else {
                    values.push(0);
                }
            }
            $('#container').highcharts({
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Column chart with negative values'
                },
                xAxis: {

                },
                credits: {
                    enabled: false
                },
                series: [{
                    data: values
                }]
            });
        });
    });
});