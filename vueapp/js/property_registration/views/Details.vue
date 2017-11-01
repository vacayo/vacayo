<template>
  <el-form :model="property" :rules="rules" ref="property" label-width="100px" label-position="top">
    <div class="title">Property Details</div>
    <div class="subtitle">Please describe your property.</div>
    <el-row :gutter="50">
      <el-col :sm="24" :md="12">
        <el-form-item label="Bedrooms" prop="bedrooms">
          <el-input-number :value="property.bedrooms" @input="update('bedrooms', $event)" :step="1" size="large"></el-input-number>
        </el-form-item>
      </el-col>
      <el-col :sm="24" :md="12">
        <el-form-item label="Bathrooms" prop="bathrooms">
          <el-input-number :value="property.bathrooms" @input="update('bathrooms', $event)" :step="0.5" size="large"></el-input-number>
        </el-form-item>
      </el-col>
    </el-row>
    <!--
    <el-select :value="property.bedrooms" @input="update('bedrooms', $event)" placeholder="Select">
      <el-option
        v-for="item in bedroom_options"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
    </el-select>
    <el-select :value="property.bathrooms" @input="update('bathrooms', $event)" placeholder="Select">
      <el-option
        v-for="item in bathroom_options"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
    </el-select>
    -->
    <el-row :gutter="50">
      <el-col :sm="24" :md="12">
        <el-form-item label="Home Type" prop="home_type">
          <el-select :value="property.home_type" @input="update('home_type', $event)" placeholder="Select" size="large">
            <el-option
              v-for="item in home_type_options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </el-form-item>
      </el-col>
      <el-col :sm="24" :md="12">
        <el-form-item label="Size (sq. ft.)" prop="home_size">
          <el-input-number :value="property.home_size" @input="update('home_size', $event)" :step="10" size="large"></el-input-number>
        </el-form-item>
      </el-col>
    </el-row>
    <el-row :gutter="50">
      <el-col :sm="24" :md="12">
        <el-form-item label="Has this property been rented before?">
          <el-switch :value="property.has_rented" @input="update('has_rented', $event)" on-text="Yes" on-color="#13ce66" off-text="No" off-color="#bfcbd9" size="large"></el-switch>
        </el-form-item>
      </el-col>
      <el-col :sm="24" :md="12">
        <el-form-item v-if="property.has_rented" label="Last Monthly Rent?" prop="last_rent">
          <el-input-number :value="property.last_rent" @input="update('last_rent', $event)" :step="10" size="large"></el-input-number>
        </el-form-item>
      </el-col>
    </el-row>
    <el-row :gutter="50">
      <el-col :sm="24" :md="12">
        <el-form-item label="Available Starting" prop="available_date">
          <el-date-picker :value="property.available_date" @input="update('available_date', $event)" type="date" placeholder="Pick a day" size="large">
          </el-date-picker>
        </el-form-item>
      </el-col>
    </el-row>
    <div class="actions">
      <el-button @click="prev">Prev</el-button>
      <el-button type="primary" @click="next">Next</el-button>
    </div>
  </el-form>
</template>

<script type="text/babel">
  import fetch from 'isomorphic-fetch';

  export default {
    data() {
      return {
        property: this.$store.state.property,
        bedroom_options: [
          {value: 0, label: 'Studio'},
          {value: 1, label: '1 Bedroom'},
          {value: 2, label: '2 Bedrooms'},
          {value: 3, label: '3 Bedrooms'},
          {value: 4, label: '4 Bedrooms'},
          {value: 5, label: '5 Bedrooms'},
          {value: 6, label: '6 Bedrooms'},
          {value: 7, label: '7+ Bedrooms'},
        ],
        bathroom_options: [
          {value: 1.0, label: '1 Bathroom'},
          {value: 1.5, label: '1.5 Bathrooms'},
          {value: 2.0, label: '2 Bathrooms'},
          {value: 2.5, label: '2.5 Bathrooms'},
          {value: 3.0, label: '3 Bathrooms'},
          {value: 3.5, label: '3.5 Bathrooms'},
          {value: 4.0, label: '4+ Bathrooms'},
        ],
        home_type_options: [
          {value: 'SingleFamily', label: 'Single Family'},
          {value: 'Duplex', label: 'Duplex'},
          {value: 'Triplex', label: 'Triplex'},
          {value: 'Quadruplex', label: 'Quadruplex'},
          {value: 'Condominium', label: 'Condominium'},
          {value: 'Cooperative', label: 'Cooperative'},
          {value: 'Mobile', label: 'Mobile'},
          {value: 'Apartment', label: 'Apartment'},
          {value: 'Timeshare', label: 'Timeshare'},
        ],
        rules: {
          bedrooms: [
            { required: true, type: 'number', message: 'Please enter the number of bedrooms in the property', trigger: 'blur' },
          ],
          bathrooms: [
            { required: true, type: 'number', message: 'Please enter the number of bathrooms in the property', trigger: 'blur' },
          ],
          home_type: [
            { required: true, type: 'string', message: 'Please select a home type', trigger: 'change' }
          ],
          home_size: [
            { required: true, type: 'number', message: 'Please enter the home size in square feet of the property', trigger: 'blur' },
          ],
          last_rent: [
            { required: false, type: 'number', message: 'Please enter a number'}
          ],
          available_date: [
            { required: true, type: 'date', message: 'Please pick a date', trigger: 'change' }
          ]
        },
      }
    },
    methods: {
      update(field, value) {
        this.$store.commit('updateProperty', {[field]: value});
      },
      next() {
        this.$refs['property'].validate((valid) => {
          if (!valid) {
            return false;
          }
          this.$router.push({name: 'offer'});
        });
      },
      prev() {
        this.$router.push({name: 'lookup'});
      },
    }
  }
</script>

<style>
</style>