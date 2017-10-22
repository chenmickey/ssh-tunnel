/**
 * @author v.lugovsky
 * created on 16.12.2015
 */
(function () {
    'use strict';

    angular.module('BlurAdmin.pages', [
        'ui.router',

        'BlurAdmin.pages.dashboard',
        'BlurAdmin.pages.ui',
        'BlurAdmin.pages.components',
        'BlurAdmin.pages.form',
        'BlurAdmin.pages.tables',
        'BlurAdmin.pages.charts',
        'BlurAdmin.pages.maps',
        'BlurAdmin.pages.profile',
    ]).config(routeConfig);

    /** @ngInject */
    function routeConfig($urlRouterProvider, baSidebarServiceProvider) {
        $urlRouterProvider.otherwise('/dashboard');

        baSidebarServiceProvider.addStaticItem({
            title  : 'Pages',
            icon   : 'ion-document',
            subMenu: [
                {
                    title    : 'Sign In',
                    fixedHref: 'auth.html',
                    blank    : true
                },
                {
                    title    : 'Sign Up',
                    fixedHref: 'reg.html',
                    blank    : true
                },
                {
                    title   : 'User Profile',
                    stateRef: 'profile'
                },
                {
                    title    : '404 Page',
                    fixedHref: '404.html',
                    blank    : true
                }
            ]
        });

        baSidebarServiceProvider.addStaticItem({
            title  : '系统维护',
            icon   : 'ion-settings',
            subMenu: [
                {
                    title   : '远程协助',
                    disabled: true,
                    stateRef: 'autossh',
                    blank   : true
                },
                {
                    title   : '系统升级',
                    disabled: true
                },
                {
                    title   : '进程管理',
                    disabled: true
                },
                {
                    title   : '证书管理',
                    disabled: true
                },
                {
                    title   : 'ip配置',
                    disabled: true
                },
                {
                    title   : '数据库备份',
                    disabled: true
                }
            ]
        });


        baSidebarServiceProvider.addStaticItem({
            title  : 'Menu Level 1',
            icon   : 'ion-ios-more',
            subMenu: [
                {
                    title   : 'Menu Level 1.1',
                    disabled: true
                },
                {
                    title  : 'Menu Level 1.2',
                    subMenu: [
                        {
                            title   : 'Menu Level 1.2.1',
                            disabled: true
                        }
                    ]
                }
            ]
        });
    }

})();
