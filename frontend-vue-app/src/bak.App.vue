<template>
  <div id="app" class="container-fluid">
    <PlaceForm ref="placeForm" @submit="submitForm" />

    <div class="card">
      <div class="card-header">
        Overview places
      </div>
      <div class="card-body">

        <div class="table-responsive">
        <table class="table table-bordered table-striped table-secondary">
          <thead>
            <th>ID</th>
            <th>Name</th>
            <th>Description</th>
            <th>Has Coffee</th>
            <th>Has Food</th>
            <th>Has Wifi</th>
            <th>Latitude</th>
            <th>Longtitude</th>
            <th>Actions</th>
          </thead>
          <tbody>
          <tr v-for="place in places" :key="place.id">
            <td>{{ place.id }}</td>
            <td>{{ place.name }}</td>
            <td>{{ place.description }}</td>
            <td>{{ place.coffee }}</td>
            <td>{{ place.food }}</td>
            <td>{{ place.wifi }}</td>
            <td>{{ place.lat }}</td>
            <td>{{ place.lng }}</td>
            <td>
              <div class="btn-group" role="group" aria-label="Basic example">
                <button type="button"
                        class="btn btn-primary"
                        @click="getPlace(place.id)">Detail</button>
                <button type="button"
                        class="btn btn-secondary"
                        @click="editPlace(place.id)">Edit</button>
                <button type="button"
                        class="btn btn-danger"
                        @click="deletePlace(place.id)">Delete</button>
              </div>
            </td>
          </tr>

          </tbody>
        </table>
      </div>
    </div>
    </div>

  </div>
</template>

<script>
import PlaceForm from "@/components/CreatePlaceForm";
import axios from "axios";

export default {
  name: "App",
  // Properties returned from data() become reactive state
  // and will be exposed on `this`.
  data() {
      return {
        places: []
      }
  },
  components: {
    PlaceForm
  },

  // Methods are functions that mutate state and trigger updates.
  // They can be bound as event handlers in templates.
  methods: {
    submitForm(placeData){
      //const self = this;
      console.log('submitForm() called')
      console.log(`placeData: ${placeData}`)
      axios.post("http://localhost:5000/places", placeData).then((response) => {
         console.log("Data submitted successfully", response.data);
         //self.resetForm();
        this.places.push(response.data);

      })
      .catch((error) => {
        console.error("Error submitting data", error);
      });
      // reset placeform
      this.$refs.placeForm.resetForm();
    },

    get_places(){
      axios.get("http://localhost:5000/places").then((response) => {
        console.log(response.data)
        this.places = response.data;
      })
    },
  },

  // Lifecycle hooks are called at different stages
  // of a component's lifecycle.
  // This function will be called when the component is mounted.
  mounted() {
    console.log(`The initial count is `);
    this.get_places();
  },
}
</script>

<style>
  /* Global styles */
</style>
