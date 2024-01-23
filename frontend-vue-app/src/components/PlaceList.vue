<template>

  <div class="container-fluid">
    <h1>List of places</h1>

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
                        @click="getPlaceDetail(place.id)">Detail</button>
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
import {onMounted, ref, defineProps, defineEmits } from 'vue'

// eslint-disable-next-line no-unused-vars
const props = defineProps({
  places: ref([]),
})

// declare emitted events
const emit = defineEmits(['get_place_detail', 'delete_place', 'edit_place'])

// emit 'get_place_detail' event with arg
const getPlaceDetail = (id) => {
  console.log(`about to emit place_detail event with arg ${id}`)
  emit('get_place_detail', id)
}

const editPlace = (id) => {
  console.log(`about to emit edit_place event with arg ${id}`)
  emit('edit_place', id)
}

const deletePlace = (id) => {
  console.log(`about to emit delete_place event with arg ${id}`)
  emit('delete_place', id)
}

onMounted(() => {
  console.log("list component is ready")
});
</script>

<style scoped>

</style>