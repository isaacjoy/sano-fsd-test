<template>
    <LoggedinSidebarTemplate page_name="research">
        <template v-slot:main-content>
            <div class="max-w-xl mx-auto mb-10 sm:mb-0 min-h-screen">
                <div class="max-w-xl mx-auto lg:px-4">
                <div id="explanation" ref="explanation" class="relative w-full" tabindex="-1" style="top: -4.2rem;"></div>

                    <section id="core-data" class="sect">
                        <div class="flex items-center w-full mb-2">
                            <!-- eslint-disable-next-line max-len --><!-- prettier-ignore -->
                            <div class="sano-border-shine sano-border-shine-orange bg-white w-7 h-7 rounded mr-3 flex flex-col justify-center items-center">
                                <svg class="pl-px w-5 h-3 relative sano-svg-red-orange z-10">
                                    <use xlink:href="#sano-symbol" />
                                </svg>
                            </div>
                            <h2 class="text-sano-burgundy text-xl">
                                My Studies
                            </h2>
                        </div>
                        <!-- On reflection I should have put the following in a table  -->
                        <div class="invisible md:visible w-full flex flex-row items-center p-4">
                            <div class="w-1/2">
                                <h1>Study</h1>
                            </div>
                            <div class="w-1/4">
                                <h1>Status</h1>
                            </div>
                             <div class="w-1/4">
                                <h1>Actions</h1>
                            </div>
                        </div>
                        <div class=" flex flex-col">
                            <div v-for="(study, index) in studies" :key=index>
                               <div  class="py-4 md:px-6 flex flex-col md:flex-row shadow w-full relative pb-12 md:pb-4 mb-8 md:mb-0" :class="{'underBorder':index==0}">
                                    <div class="w-full pt-4 md:pt-0 text-left md:w-1/2 bg-white">
                                        <h1 class="font-semibold pb-1">{{study.title}}</h1>
                                        <h1 class="text-sm">Run by Sano Genetics</h1>
                                    </div>
                                    <div style="border-left:1px solid orange; border-right:1px solid orange;" class="w-full md:w-1/4 centerize ">
                                        <div v-if="index%2 == 0" class="w-full md:w-2/3 flex justify-between flex-row md:flex-col absolute top-0 left-0 md:relative">
                                            <h1 style="color:darkorange" class="font-semibold">Enrolled</h1>
                                            <h1 style="background:blue;width:130px; " class="text-white text-center md:mt-2 py-1 w-1/2 bg-green-400 rounded-lg">Complete</h1>
                                        </div>
                                        <div v-else class="w-full  md:w-2/3  flex justify-between flex-row md:flex-col absolute top-0 left-0 md:relative">
                                            <h1  style="color:darkorange"  class="font-semibold">Not enrolled</h1>
                                        </div>
                                    </div>
                                    <div class="w-full md:w-1/4 centerize absolute md:relative bottom-0 ">
                                        <div v-if="enrollments.includes(study.id)" class="w-full md:w-2/3 ">
                                            <button @click="leaveStudy(study.id)" style="background:pink;" class="w-full px-6 py-2 rounded">Leave study</button>
                                        </div>
                                        <div class="w-full md:w-2/3 "  v-else>
                                            <button @click="joinStudy(study.id)" style="background:orange;" class="w-full px-6 py-2 rounded">Join study</button>
                                        </div>
                                    </div>
                               </div>
                            </div>
                        </div>
                    </section>
                </div>
            </div>
        </template>
        <template v-slot:sidebar-content>
        </template>
    </LoggedinSidebarTemplate>
</template>

<script>

import LoggedinSidebarTemplate from "@/layouts/LoggedinSidebarTemplate";

export default {
    name: "Research",
    components: {
        LoggedinSidebarTemplate,
    },
    data: function() {
        return {
            enrollments: [],
            studies: []
        }
    },
    created() {
        let that = this
        this.$api.user
            .get_enrollments()
            .then((response) => {
                this.enrollments = response.data
            })
        this.$api.pub
            .get_studies()
            .then((response) => {
                this.studies = response.data
            })
    },
    methods: {
        joinStudy(id) {
            this.$api.user
                .enroll(id)
                .then((response) => {
                     this.$router.go("/research")
                })
        },
        leaveStudy(id) {
            this.$api.user
                .unenroll(id)
                .then((response) => {
                     this.$router.go("/research")
                })
        }
    }
};
</script>

<style scoped lang="scss">


.centerize {
    @apply flex justify-center items-center content-center;
}

.mobile-sticky {
    top: 1rem;
}

.sect {
    @apply relative mt-6 mx-4 px-4 py-6 border border-sano-pink rounded overflow-hidden bg-white;
    @media (min-width: 992px) {
        @apply p-8 mx-0;
    }
}

@media (max-width: 575px) {
    .mobile-sticky {
        @apply sticky bg-white -ml-4 px-4 border-b border-sano-pink;
        z-index: 99;
        top: 0;
        width: calc(100% + 2rem);
    }

    .sano-toggle-label.sano-toggle-label {
        padding: 0 0.75rem;
    }
}
</style>
