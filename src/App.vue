<template>
  <v-app m-0>
    <v-layout row>
      <v-flex xs12>
        <v-card>
          <v-toolbar flat dark color="orange darken-3">
            <v-toolbar-title>
              <v-icon>camera</v-icon>
              Computación Fisica
            </v-toolbar-title>
          </v-toolbar>
          <v-subheader>
            Fotos tomadas
          </v-subheader>
          <v-container fluid grid-list-sm>
            <v-layout row wrap>
              <v-flex v-for="(photo, index) in photos" :key="index" xs4>
                <v-tooltip bottom>
                  <img slot="activator" :src="photo.photoLink" class="image" :alt="photo.photoName" width="100%" height="100%">
                  <span>Fue tomada el {{ photo.photoName }}</span>
                </v-tooltip>
              </v-flex>
            </v-layout>
          </v-container>
          <v-footer class="mt-5"></v-footer>
        </v-card>
      </v-flex>
    </v-layout>
  </v-app>
</template>


<script>

import db from './services/firestore.service'
import storage from './services/storage.service'
export default {
  name: 'App',
  data () {
    return {
      photos: []
    }
  },
  methods: {
    onPhotosSnapshot() {
      db.collection("photos").orderBy("takeTime", "desc").onSnapshot(photos => {
        // this.$toasted.show('Se tomó una nueva foto')
        this.photos = []
        photos.docs.forEach(picture => {
          const { photoName, takeTime } = picture.data()
          
          this.getPhotoPublicLink(`${photoName}`)
            .then(photoLink => {
              console.log({ photoLink })
              this.photos.push({ photoName, takeTime, photoLink })
            })  
        })
      })
    },
    async getPhotoPublicLink(photoName) {
      return storage.child(photoName).getDownloadURL();
    }
  },
  mounted() {
    this.onPhotosSnapshot()
  }
}
</script>

<style>
  .list-item {
    display: inline-block;
    margin-right: 10px;
  }
  .list-enter-active, .list-leave-active {
    transition: all 1s;
  }
  .list-enter, .list-leave-to /* .list-leave-active below version 2.1.8 */ {
    opacity: 0;
    transform: translateY(30px);
  }
</style>

