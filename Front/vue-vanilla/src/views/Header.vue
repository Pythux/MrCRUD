<template>
  <div>
    <div id="crud-header" class="container-fluid text-white">
      <div class="d-flex justify-content-center text-center">
        <router-link :to="{name:'home'}">
          <h1 class="display-1" style="color: #f9f0e1;">
            Creative's Mind
          </h1>
        </router-link>
      </div>
      <div class="p-3 blockquote align-self-end">
        <footer class="blockquote-footer" style="color: #efefef">
          Mr. CRUD
        </footer>
      </div>
    </div>
  </div>
</template>

<style lang="stylus">
@import url('https://fonts.googleapis.com/css?family=Lobster&display=swap%27');

h1, h2, h3 {
    font-family: 'Lobster', cursive;
}

#crud-header {
    position: relative;
    animation-name: popheader;
    animation-duration: 1.5s;
    background-color: #ff9a8e;
}

@keyframes popheader {
    0% {
        background-color: #ff9a8e;
        left: -100%;
    }
    50% {
        background-color: #ff9a8e;
    }
    100% {
        background-color: #ff9a8e;
        // #282c34
        // #09d3ac
        left: 0%;
    }
}

a, button
    text-decoration: none
    transition-duration: 0.6s !important
    transition-property: border-radius !important
    &:hover
        border-radius: 50% !important
        text-decoration: none !important
    &:visited
        text-decoration: none !important

</style>
