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
                        { name: 'phone', label: 'Phone', field: 'phone', align: 'left', sortable: true },
                        { name: 'email', label: 'Email', field: 'email', align: 'left', sortable: true },
                        { name: 'website', label: 'Website', field: 'website', align: 'left', sortable: true },
                        { name: 'description', label: 'Description', field: 'description', align: 'left', sortable: true },
                    ]"
                    row-key="id"
                    title="Stores"
                    :separator="separator"
                    :pagination="initialPagination"
                />
            </div>
        </div>
    </div>
</template>
  
<style></style>
  
<script>
export default {
    name: 'HomePage',
    data() {
        return {
            merchant: null,
            product: [],
            store: [],
            title: 'Title: Title Title',
            initialPagination: {
                rowsPerPage: 5,
            },
            separator: 'none',
            merchants: [
                {
                    id: 1,
                    name: 'Merchant 1',
                    address: 'Address 1',
                    phone: 'Phone 1',
                    email: 'Email 1',
                    website: 'Website 1',
                    description: 'Description 1',
                },
                {
                    id: 2,
                    name: 'Merchant 2',
                    address: 'Address 2',
                    phone: 'Phone 2',
                    email: 'Email 2',
                    website: 'Website 2',
                    description: 'Description 2',
                },
                {
                    id: 3,
                    name: 'Merchant 3',
                    address: 'Address 3',
                    phone: 'Phone 3',
                    email: 'Email 3',
                    website: 'Website 3',
                    description: 'Description 3',
                }
            ],
            products: [
                {
                    id: 1,
                    name: 'Product 1',
                    description: 'Description 1',
                    price: 100,
                    merchant: 1,
                    stores: [1, 3],
                },
                {
                    id: 2,
                    name: 'Product 2',
                    description: 'Description 2',
                    price: 200,
                    merchant: 1,
                    stores: [1, 2],
                },
                {
                    id: 3,
                    name: 'Product 3',
                    description: 'Description 3',
                    price: 300,
                    merchant: 2,
                    stores: [2, 3],
                },
                {
                    id: 4,
                    name: 'Product 4',
                    description: 'Description 4',
                    price: 400,
                    merchant: 2,
                    stores: [1, 2, 3],
                },
                {
                    id: 5,
                    name: 'Product 5',
                    description: 'Description 5',
                    price: 500,
                    merchant: 3,
                    stores: [1, 3],
                },
                {
                    id: 6,
                    name: 'Product 6',
                    description: 'Description 6',
                    price: 600,
                    merchant: 3,
                    stores: [1, 2, 3],
                },
            ],
            stores: [
                {
                    id: 1,
                    name: 'Store 1',
                    address: 'Address 1',
                    phone: 'Phone 1',
                    email: 'Email 1',
                    website: 'Website 1',
                    description: 'Description 1',
                },
                {
                    id: 2,
                    name: 'Store 2',
                    address: 'Address 2',
                    phone: 'Phone 2',
                    email: 'Email 2',
                    website: 'Website 2',
                    description: 'Description 2',
                },
                {
                    id: 3,
                    name: 'Store 3',
                    address: 'Address 3',
                    phone: 'Phone 3',
                    email: 'Email 3',
                    website: 'Website 3',
                    description: 'Description 3',
                }
            ],
        }
    },
    methods: {
        getSelectedString() {
            return `${this.product[0].name} selected.`
        },
        getStoreString() {
            return `${this.store[0].name} selected.`
        },
    },
}
</script>
  