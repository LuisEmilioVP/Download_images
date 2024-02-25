document.getElementById('btnDescargar').addEventListener('click', function () {
	// Mostrar modal
	document.getElementById('modal').style.display = 'block';

	// Realizar una solicitud AJAX para obtener los nombres de las imágenes descargadas
	var xhr = new XMLHttpRequest();
	xhr.open('GET', '../descargas.json', true);
	xhr.onreadystatechange = function () {
		if (xhr.readyState == 4 && xhr.status == 200) {
			var response = JSON.parse(xhr.responseText);
			var listaDescargas = document.getElementById('listaDescargas');
			listaDescargas.innerHTML = ''; // Limpiar la lista antes de agregar nuevos elementos
			response.forEach(function (nombreArchivo) {
				var li = document.createElement('li');
				li.textContent = nombreArchivo;
				listaDescargas.appendChild(li);
			});

			// Mostrar las imágenes en la galería
			var galeria = document.getElementById('galeria');
			galeria.innerHTML = ''; // Limpiar la galería antes de agregar nuevas imágenes
			response.forEach(function (nombreArchivo) {
				var img = document.createElement('img');
				img.src = '/local_Images/' + nombreArchivo;
				img.alt = nombreArchivo;
				img.classList.add('imagen');
				galeria.appendChild(img);
			});
		}
	};
	xhr.send();
});

document.querySelector('.close').addEventListener('click', function () {
	// Cerrar modal al hacer clic en la "X"
	document.getElementById('modal').style.display = 'none';
});
