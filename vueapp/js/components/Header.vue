<template>
  <div>
    <el-row class="header" type="flex" justify="space-around">
      <el-col :xs="0" :sm="3"></el-col>
      <el-col :xs="24" :sm="18">
        <div class="logo">
          <a href="/"><img :src="logo" alt="Vacayo: Begin at Home" /></a>
        </div>
      </el-col>
      <el-col :xs="0" :sm="3"></el-col>
    </el-row>
  </div>
</template>

<script type="text/babel">
import logo from '../../img/logo.png'

export default {
  data() {
    return {
      logo: logo
    }
  },
}
</script>

<style>
.header {
  background-color: #282D33;
  height: 76px;
}

.logo img {
  height: 72px;
}
</style>
