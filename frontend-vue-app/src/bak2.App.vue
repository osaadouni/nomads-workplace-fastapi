<template>
  <div id="app" class="container-fluid">
    <PlaceForm ref="placeFormRef" @submit="submitForm" />

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

<script setup>
import { watch, ref, onMounted } from 'vue'
import PlaceForm from "@/components/CreatePlaceForm";
import axios from "axios";

const places = ref(null);
const placeFormRef = ref();

function submitForm(placeData){
  console.log('submitForm() called')
  console.log(JSON.stringify(placeData.value))

  axios.post("http://localhost:5000/places", placeData.value).then((response) => {
     console.log("Data submitted successfully", response.data);

    // call child func to reset form
    placeFormRef.value.resetForm()

    // update places
    getPlaces()

  })
  .catch((error) => {
    console.error("Error submitting data", error);
  });
}

async function getPlaces(){
  axios.get("http://localhost:5000/places")
    .then((response) => {
      console.log(response.data)
      places.value = response.data
    })
    .catch(error => {
      console.error('Error querying places', error)
    })
}

async function getPlace(place_id) {
  axios.get(`http://localhost:5000/place/${place_id}`)
    .then((response) => {
      console.log(response.data)
    })
    .catch(error => {
      console.error('Error querying place details!' , error)
    })
}

async function deletePlace(place_id) {
  axios.delete(`http://localhost:5000/place/${place_id}`)
    .then((response) => {
      console.log(response.data)
      if (response.data.success) {
        getPlaces()
      } else {
        // console.error(response.data.error)
        console.error('Some error occurred while deleting!')
      }
    })
    .catch(error => {
      console.error('Error deleting place!' , error)
    })
}

async function editPlace(place_id) {
  console.log(`editPlace(${place_id})`);
  axios.get(`http://localhost:5000/place/${place_id}`)
    .then((response) => {
      console.log(response.data)
    })
    .catch(error => {
      console.error('Error deleting place!' , error)
    })
}


onMounted(() => {
  console.log('mounted')
  getPlaces()
})
watch(places)

watch(placeFormRef)

</script>

<style>
  /* Global styles */
</style>
