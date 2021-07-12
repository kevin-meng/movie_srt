<template>
    <div class=header>
        <b-container fluid>
          <b-navbar toggleable="lg" type="dark" variant="info">
            <b-navbar-brand href="#">剧中人说</b-navbar-brand>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
              <b-navbar-nav>
                <b-nav-item :href="'/'" >主页</b-nav-item>
                <b-nav-item href="#" disabled>编辑</b-nav-item>
                <b-nav-item href="#" disabled>发布</b-nav-item>
              </b-navbar-nav>

              <!-- Right aligned nav items -->
              <b-navbar-nav class="ml-auto">
                <b-nav-form>
                  <b-form-input size="sm" class="mr-sm-2" placeholder="搜索电影名"></b-form-input>
                  <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
                </b-nav-form>

                <b-nav-item-dropdown right>
                  <!-- Using 'button-content' slot -->
                  <template #button-content>
                    <em>User</em>
                  </template>
                  <b-dropdown-item href="#">Profile</b-dropdown-item>
                  <b-dropdown-item href="#">Sign Out</b-dropdown-item>
                </b-nav-item-dropdown> 
              </b-navbar-nav>
            </b-collapse>
          </b-navbar>
        </b-container>
    </div>
</template>



<script>
export default {
    name:"Header",
    // setup(props,context) {
      
    // }
}
</script>


<style lang="scss" scoped>
.header {
    position: sticky;
    position: -webkit-sticky;
}
</style>