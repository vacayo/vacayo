<template>
  <el-row class="header" type="flex" justify="space-around">
    <el-col :span="6"> </el-col>
    <el-col :span=8>
      <div class="logo">
        <img :src="logo" alt="Vacayo: Begin at Home" />
      </div>
    </el-col>
    <el-col :span="4">
      <div class="quote">Quote: $</div>
    </el-col>
    <el-col :span="6"> </el-col>
  </el-row>
</template>

<script type="text/babel">
import logo from '../../../assets/img/vacayo-logo-horiz-white_1.png'

export default {
  data() {
    return {
      logo: logo
    }
  },

  methods: {
  }
}
</script>

<style>
.header {
  background-color: #424242;
  min-height: 76px;
  margin-bottom: 50px;
}

.logo img {
  height: 72px;
}

.quote {
  color: #EEEEEE;
  font-weight: bold;
}
</style>