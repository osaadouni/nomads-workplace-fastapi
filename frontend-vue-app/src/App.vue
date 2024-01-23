<template>
  <div id="app" class="container-fluid p-3">

    <LoginView />
    <!--
    <div class="btn-group" role="group" aria-label="Basic example">
      <button class="btn btn-outline-secondary" v-for="comp in Object.keys(appComponents)" :key="comp" @click="displayComponent(comp)">
        {{ `Show ${comp.charAt(0).toUpperCase() + comp.slice(1)} Place` }}
      </button>
    </div>
    -->

    <div class="d-flex flex-row-reverse">
    <div class="btn-group" role="group" aria-label="Basic example">
      <button v-if="appComponents.list.value"
              class="btn btn-primary"
              @click="displayComponent('create')">Create New Place</button>

      <button v-if="appComponents.detail.value"
              class="btn btn-danger"
              @click="displayComponent('delete')">Delete Place</button>
      <button v-if="showPlaceListBtn"
              class="btn btn-primary"
              @click="displayComponent('list')">Back to overview</button>
    </div>
    </div>

    <CreatePlaceForm v-if="appComponents.create.value"
                      ref="placeFormRef"
                      @submit="submitForm "/>

    <EditPlaceForm v-if="appComponents.edit.value"
                   :data="formData"
                   @delete_place="(place_id) => apiDeletePlace(place_id)"
                   @submit="updateForm"/>

    <PlaceDetail v-if="appComponents.detail.value"
                 :data="apiPlaceDetail"
                 @delete_place="(place_id) => apiDeletePlace(place_id)" />
    <PlaceList v-if="appComponents.list.value"
               ref="placeListRef"
               :places="placeData"
               @delete_place="(place_id) => apiDeletePlace(place_id)"
               @get_place_detail="(place_id) => apiGetPlaceDetail(place_id)"
               @edit_place="(place_id) => apiEditPlace(place_id)"
    />


  </div>
</template>

<script setup>
// eslint-disable-next-line no-unused-vars
import {watch, ref, onMounted, computed} from 'vue'
import CreatePlaceForm from "@/components/CreatePlaceForm";
import EditPlaceForm  from "@/components/EditPlaceForm";
import PlaceDetail  from "@/components/PlaceDetail";
import PlaceList from "@/components/PlaceList";
import LoginView from "@/components/LoginView";

import apiRequests from "@/components/apiRequests";


const { apiPlaces, apiGetPlaceList, apiAddPlace, apiPlaceCreated,
  apiGetPlaceDetail, apiPlaceDetail, apiPlaceDetailFetched , apiDeletePlace,
  apiEditPlaceFormData, apiEditPlaceEnabled, apiEditPlace,
  apiUpdatePlace, apiPlaceUpdated } = apiRequests();

const placeData = ref([]);
const placeFormRef = ref();
const formData = ref({});

const appComponents = { create: ref(false), edit: ref(false), detail: ref(false), list: ref(false), delete: ref(false)};
const displayComponent = (comp) => {
  Object.keys(appComponents).forEach(key => appComponents[key].value = key === comp);
};

const showPlaceListBtn = computed(() => {
  return (
      appComponents.create.value ||
      appComponents.edit.value ||
      appComponents.detail.value ||
      appComponents.delete.value)
});

/*
 * Define place watchers
 */

// Watcher: Get place updates
watch(apiPlaces, (newPlaces) => {
  console.log(`==> places is updated: len=${newPlaces.length}`)
  placeData.value = newPlaces;
  displayComponent('list')
})

// Watcher: new place created
watch(apiPlaceCreated, (isCreated, oldValue) => {
  console.log(`new place created: ${isCreated};  oldValue: ${oldValue}`)
  if (isCreated) {
    // displayComponent('list');
    apiGetPlaceList();
  }
})

// Watcher: place detail requested
watch(apiPlaceDetailFetched, (isDetailRefreshed) => {
  console.log(`new place detail fetched: ${isDetailRefreshed}`)
  if (isDetailRefreshed) {
    displayComponent('detail')
  }
})

// Watcher: edit place detail requested
watch(apiEditPlaceFormData, (newData) => {
  console.log(`newData: ${newData}`)
    formData.value = newData;
    displayComponent('edit')
})
watch(apiEditPlaceEnabled, (isEnabled) => {
  console.log(`isEnabled: ${isEnabled}`)
})

watch(apiPlaceUpdated, (isUpdated) => {
  console.log(`isUpdated: ${isUpdated}`)
  apiGetPlaceList();
})

function submitForm(placeData){
  console.log('submitForm() called')
  apiAddPlace(placeData);
}

function updateForm(placeData){
  console.log('updateForm() called')
  apiUpdatePlace(placeData)
}

onMounted(() => {
  console.log('mounted');
  //displayComponent('list')
  apiGetPlaceList()
})
// watch(places)
// watch(placeFormRef)

</script>

<style>
  /* Global styles */
</style>
