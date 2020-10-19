<script type="text/javascript" src="webcam.js"/>

function take_snapshot() {
	Webcam.snap(function (data_uri) {
		document.getElementById('my_result').innerHTML = '<img src="' + data_uri + '"/>';
		const predictURL = '/image'
		const sendPkg = {
			imgBase64: `${data_uri}`
		};

		var request = $.ajax({
			type: "POST",
			url: predictURL,
			data: JSON.stringify(sendPkg),
			contentType: "application/json",
			statusCode: {
				200: () => console.log('ajax call receives response')
			},
		});

		request.done(function (resp) {
			console.log(`receive msg from server ${resp.response}`);
			var response = resp.response;
			document.getElementById('prediction').innerHTML = response;
		});

		request.fail(function (jqXHR, textStatus) {
			console.log(`Request failed: " + ${textStatus}`);
		});

	});
}