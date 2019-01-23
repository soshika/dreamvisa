 // This example displays a marker at the center of india.
 // When the user mouseover the marker, an info window opens.

 function initMap() {
     var iran = {lat: 36.334225, lng: 59.491096};
     var map = new google.maps.Map(document.getElementById('map'), {
         zoom: 10,
         center: iran
     });

     var contentString = '<div class="info_content">' +
         '<h3 class="info_location_name">سبزگستر</h3>' +
         '<p class="info_location_text">بلوار فرهنگ - فرهنگ ۴۳ - انوشیروان ۷ - پلاک ۶۰</p>' +
         '<p class="info_location_call"><span><i class="fa fa-phone"></i></span>(۰۵۱) ۳۸۶۴۵۴۹۴</p>' +
         '<a href="#" class="btn-link">View Location</a>' +


         '</div>';

     var infowindow = new google.maps.InfoWindow({
         content: contentString
     });

     var marker = new google.maps.Marker({
         position: india,
         map: map,
         title: 'ایران (سبزگستر)'
     });
     marker.addListener('mouseover', function() {
         infowindow.open(map, marker);
     });
     // show map, open infoBox 
     google.maps.event.addListenerOnce(map, 'tilesloaded', function() {
         infowindow.open(map, marker);
     });

 }