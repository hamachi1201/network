<template>
  <eg-renderer
    ref="gene"
    id="gene"
    node-id-property="id"
    node-label-property="name"
    link-type-property="$none"
    default-node-width="2"
    default-node-height="2"
    default-node-fill-color="#000"
    default-node-stroke-width="2"
    default-node-label-stroke-width="0.6"
    default-node-label-fill-color="#FFFFFF"
    default-node-label-stroke-color="#000000"
    default-node-label-font-family="helvetica"
    default-link-stroke-width="0.3"
    default-link-stroke-color="#888"
    transition-duration="1000"
    layout-method="fmmm"
    v-on:click="handleClick"
    v-on:nodemouseenter="handleNodeMouseEnter"
    v-on:nodemouseleave="handleNodeMouseLeave"
  ></eg-renderer>
</template>

<script>

import '@webcomponents/custom-elements'
import 'eg-renderer'
import {
  Graph,
  FMMMLayout
} from 'emogdf'
import egraph from '../egraph'
