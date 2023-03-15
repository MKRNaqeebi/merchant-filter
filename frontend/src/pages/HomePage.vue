<template>
    <div class="q-pa-md">
        <!-- title in center -->
        <div class="text-h4 text-center">{{ title }}</div>
        <div class="row">
            <div class="col-4">
                <!-- select merchant from select -->
                <q-select
                    v-model="merchant"
                    :options="merchants"
                    option-value="name"
                    option-label="name"
                    label="Select Merchant"
                />
                <!-- show merchant info in card -->
                <div class="q-pa-md" v-if="merchant">
                    <q-card>
                        <q-card-section>
                            <div class="text-h6">{{ merchant.name }}</div>
                            <div class="text-h6">{{ merchant.address }}</div>
                            <div class="text-h6">{{ merchant.phone }}</div>
                            <div class="text-h6">{{ merchant.email }}</div>
                            <div class="text-h6">{{ merchant.website }}</div>
                            <div class="text-h6">{{ merchant.description }}</div>
                        </q-card-section>
                    </q-card>
                </div>
            </div>
            <div class="col-4">
                <!-- show products in table belonging to selected merchant -->
                <q-table
                    v-if="merchant"
                    :rows="products.filter(product => product.merchant == merchant.id)"
                    :columns="[
                        { name: 'name', label: 'Name', field: 'name', align: 'left', sortable: true },
                        { name: 'description', label: 'Description', field: 'description', align: 'left', sortable: true },
                        { name: 'price', label: 'Price', field: 'price', align: 'left', sortable: true },
                    ]"
                    row-key="id"
                    selection="single"
                    title="Products"
                    :separator="separator"
                    :selected-rows-label="getSelectedString"
                    :pagination="initialPagination"
                    v-model:selected="product"
                />
            </div>
            <div class="col-4">
                <!-- show stores in table belonging to selected product -->
                <q-table
                    v-if="product.length"
                    :rows="stores.filter(store => product[0].stores.includes(store.id))"
                    :columns="[
                        { name: 'name', label: 'Name', field: 'name', align: 'left', sortable: true },
                        { name: 'address', label: 'Address', field: 'address', align: 'left', sortable: true },
                        { name: 'website', label: 'Website', field: 'website', align: 'left', sortable: true },
                    ]"
                    row-key="id"
                    selection="single"
                    title="Stores"
                    :separator="separator"
                    :selected-rows-label="getStoreString"
                    :pagination="initialPagination"
                    v-model:selected="store"
                />
                <!-- text input from user -->
                <q-input
                    v-if="store.length"
                    v-model="inputType"
                    label="Input Type"
                    filled
                    clearable
                />
                <!-- button to submit input -->
                <q-btn
                    v-if="store.length"
                    color="primary"
                    label="Submit"
                    @click="postStoreInfo(store[0].id)"
                />
            </div>
        </div>
    </div>
</template>
  
<style></style>
  
<script>
import axios from 'axios';

export default {
    name: 'HomePage',
    data() {
        return {
            merchant: null,
            product: [],
            store: [],
            inputType: '',
            title: 'Title: Title Title',
            initialPagination: {
                rowsPerPage: 5,
            },
            separator: 'none',
            merchants: [],
            products: [],
            stores: [],
        }
    },
    beforeMount() {
        this.getData();
    },
    methods: {
        getSelectedString() {
            return `${this.product[0].name} selected.`
        },
        getStoreString() {
            return `${this.store[0].name} selected.`
        },
        getData() {
            axios.get('/api/config')
                .then(response => {
                    this.merchants = response.data.merchants;
                    this.products = response.data.products;
                    this.stores = response.data.stores;
                    this.title = response.data.title;
                })
                .catch(error => {
                    console.log(error);
                });
        },
        postStoreInfo(storeId) {
            axios.post('/api/stores', {
                inputtype: this.inputType,
                store: storeId,
            })
                .then(response => {
                    console.log(response.data);
                })
                .catch(error => {
                    console.log(error);
                });
        },
    },
}
</script>
  