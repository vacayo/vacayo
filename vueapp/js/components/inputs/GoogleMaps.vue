<template>
  <div class="google-map" :id="mapName">
    <span>{{ radius }}</span>
    <span>{{ location.address }}</span>
  </div>
</template>

<script type="text/babel">
  import markerIcon from '../../../img/ic_person_pin_circle_black_48dp_2x.png'


  export default {
    name: 'GoogleMaps',
    model: {
      prop: 'location',
      event: 'input'
    },
    props: {
      location: Object,
      name: String,
      radius: Number
    },
    components: {},
    methods: {
      createMap(element) {
        let map = this.map = new google.maps.Map(element, {
          center: this.position,
          draggable: true,
          zoomControl: true,
          mapTypeControl: false,
          scaleControl: true,
          streetViewControl: false,
          rotateControl: false,
          fullscreenControl: false,
          zoom: 10
        });

        // Add circle overlay and bind to marker
        let circle = this.circle = new google.maps.Circle({
          map,
          center: this.position,
          radius: 1609.34 * this.radius, // 1609.34 meters in 1 mile
          geodesic: true,
          editable: false,
          draggable: false,
          fillColor: "#F00",
          fillOpacity: 0.2,
          strokeColor: 'white',
          strokeWeight: 0.5
        });
        circle.bindTo('center', map, 'center');

        let marker = this.marker = new google.maps.Marker({
          title: 'My coverage area',
          animation: google.maps.Animation.DROP,
          icon: {
            url: markerIcon,
            size: new google.maps.Size(32, 32),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(16, 16),
            scaledSize: new google.maps.Size(32, 32)
          },
          map
        });
        marker.bindTo('position', map, 'center');

        map.addListener('dragend', function () {
          let position = map.getCenter();
          circle.setCenter(position);
          this.$emit('input', {
            'address': null,
            latitude: Number((position.lat()).toFixed(4)),
            longitude: Number((position.lng()).toFixed(4)),
          });
        }.bind(this));
      },
      updatePosition() {
        // Coordinated provided
        if (this.location.latitude && this.location.longitude) {
          this.position = new google.maps.LatLng(this.location.latitude, this.location.longitude);
        }
        // Attempt geolocation
        else if (navigator.geolocation && window.location.protocol == "https:") {
          navigator.geolocation.getCurrentPosition(function (position) {
            this.position = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
          }.bind(this), function () {});
        }
        // default to NYC
        else {
          this.position = new google.maps.LatLng(40.7128, -74.0060);
        }

        if (this.map) {
          this.map.setCenter(this.position)
        }
      },
      updateRadius() {
        this.circle.setRadius(1609.34 * this.radius);
      }
    },
    data: function () {
      return {
        mapName: this.name + "-map",
        map: null,
        marker: null,
        circle: null,
        position: null
      }
    },
    created: function () {
      this.updatePosition()
    },
    mounted: function () {
      const element = document.getElementById(this.mapName);
      this.createMap(element);
    },
    updated: function () {
      this.updateRadius();
      this.updatePosition();
    }
  }
</script>

<style>
  .google-map {
    width: 100%;
    min-height: 400px;
    margin: 0 auto;
    background: gray;
  }
</style>