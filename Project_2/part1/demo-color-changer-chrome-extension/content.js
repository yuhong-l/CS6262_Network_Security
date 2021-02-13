var x = document.getElementsByTagName("a"); // try all headings
// further try for links too, replace 'h1' by 'a'
var i = 0,
    k = x.length;

if (config == 'red') {
    for (var i = 0; i < k; i++) {
        x[i].style.color = 'red';
    }
} else if (config == 'blue') {
    for (var i = 0; i < k; i++) {
        x[i].style.color = 'blue';
    }
} else if (config == 'green') {
    for (i = 0; i < k; i++) {
        x[i].style.color = 'green';
    }
} else if (config == 'purple') {
    for (var i = 0; i < k; i++) {
        x[i].style.color = 'purple';
    }
}
