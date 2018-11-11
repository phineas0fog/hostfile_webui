function onKeySearch() {
    // Declare variables
    var input, filter, table, tr, td, i;
    input = document.getElementById("searchBar");
    filter = input.value.toUpperCase();
    table = document.getElementById("hosts_list");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
	td = tr[i].getElementsByTagName("td")[2];
	if (td) {
	    if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
		tr[i].style.display = "";
	    } else {
		tr[i].style.display = "none";
	    }
	}
    }
}

function sendNewRule() {
    var address = document.getElementById('newRuleAddress').value;
    var hostname = document.getElementById('newRuleHostname').value;
    console.log(address);
    console.log(hostname);

    axios.post('/api/hosts', {
	address: address,
	hostname: hostname
    })
	.then(function (response) {
	    window.location.reload(false);
	})
	.catch(function (error) {
	    console.log(error);
	});
}
