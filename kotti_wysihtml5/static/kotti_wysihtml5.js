// JSLint options
/*global $, jQuery, wysihtml5*/
"use strict";

var kotti_wysihtml5 = {};

(function ($, wysihtml5) {

    kotti_wysihtml5.init = function (node) {
        $(node).wysihtml5({
            toolbar: {
                'browser':
                    '<li>' +
                    '<div id="browserModal" class="modal hide fade" tabindex="-1" role="dialog" aria-hidden="true">' +
                    '<div class="modal-header">' +
                    '<button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button>' +
                    '<h3>Browse</h3>' +
                    '</div>' +
                    '<div class="modal-body"></div>' +
                    '<div class="modal-footer"></div>' +
                    '</div>' +
                    '<a class="btn" data-wysihtml5-command="openBrowser">' +
                    '<i class="icon-folder-open"></i>' +
                    '</a>' +
                    '</li>'
            }
        });
    };

    wysihtml5.commands.openBrowser = {
        exec: function (composer, command) {
            var $browser, kotti_url;

            $browser = $('#browserModal');
            $browser.on('shown', function () {
                $(this).on('click', 'a', function (e) {
                    e.preventDefault();
                    $browser.find('.modal-body').load(this.href);
                })
            });

            kotti_url = window.location.toString();
            kotti_url = kotti_url.replace(/@@edit/, "@@kottibrowser");
            $browser.modal({
                remote: kotti_url
            });
        }
    };

}(jQuery, wysihtml5));
