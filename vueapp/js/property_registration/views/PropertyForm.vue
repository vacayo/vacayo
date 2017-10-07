<template>
  <el-form :model="property" :rules="rules" ref="property" label-width="100px" label-position="top">
    <div v-if="this.property.in_service">
      <div class="title">Property Details</div>
      <div class="subtitle">Please describe your property.</div>
      <el-row :gutter="50">
        <el-col :sm="24" :md="12">
          <el-form-item label="Bedrooms" prop="bedrooms">
            <el-input-number :value="property.bedrooms" @input="updateProperty('bedrooms', $event)" :step="1" size="large"></el-input-number>
          </el-form-item>
        </el-col>
        <el-col :sm="24" :md="12">
          <el-form-item label="Bathrooms" prop="bathrooms">
            <el-input-number :value="property.bathrooms" @input="updateProperty('bathrooms', $event)" :step="0.5" size="large"></el-input-number>
          </el-form-item>
        </el-col>
      </el-row>
      <!--
      <el-select :value="property.bedrooms" @input="updateProperty('bedrooms', $event)" placeholder="Select">
        <el-option
          v-for="item in bedroom_options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      <el-select :value="property.bathrooms" @input="updateProperty('bathrooms', $event)" placeholder="Select">
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
            <el-select :value="property.home_type" @input="updateProperty('home_type', $event)" placeholder="Select" size="large">
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
            <el-input-number :value="property.home_size" @input="updateProperty('home_size', $event)" :step="10" size="large"></el-input-number>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row :gutter="50">
        <el-col :sm="24" :md="12">
          <el-form-item label="Has this property been rented before?">
            <el-switch :value="property.has_rented" @input="updateProperty('has_rented', $event)" on-text="Yes" on-color="#13ce66" off-text="No" off-color="#bfcbd9" size="large"></el-switch>
          </el-form-item>
        </el-col>
        <el-col :sm="24" :md="12">
          <el-form-item v-if="property.has_rented" label="Last Monthly Rent?" prop="last_rent">
            <el-input-number :value="property.last_rent" @input="updateProperty('last_rent', $event)" :step="10" size="large" v-mask="'$####.00'"></el-input-number>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row :gutter="50">
        <el-col :sm="24" :md="12">
          <el-form-item label="Available Starting" prop="available_date">
            <el-date-picker :value="property.available_date" @input="updateProperty('available_date', $event)" type="date" placeholder="Pick a day" size="large">
            </el-date-picker>
          </el-form-item>
        </el-col>
      </el-row>
      <div class="actions">
        <el-button @click="prev">Prev</el-button>
        <el-button type="primary" @click="next">Next</el-button>
      </div>
    </div>
    <div v-else>
      <div class="title">We're sorry, but we're not in your area yet!</div>
      <div class="subtitle">
        We’re working to expand our services across the nation.
        <br /><br />
        We can notify you when we arrive at your area, if you leave your contact information.
      </div>
      <div class="actions">
        <el-button @click="prev">Prev</el-button>
        <el-button type="primary" @click="next">Leave Contact Info</el-button>
      </div>
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
      updateProperty(field, value) {
        this.$store.commit('updateProperty', {[field]: value});
      },
      next() {
        this.$refs['property'].validate((valid) => {
          if (!valid) {
            return false;
          }
          this.$emit('next');
        });
      },
      prev() {
        this.$emit('prev');
      },
    },
  }
</script>

<style>
</style>