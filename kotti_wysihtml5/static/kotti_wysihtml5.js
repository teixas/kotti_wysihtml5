// JSLint options
/*global $, jQuery*/
"use strict";

var kotti_wysihtml5 = {};

(function ($) {

    kotti_wysihtml5.init = function (node) {
        $(node).wysihtml5({
            toolbar: {
                'browser':
                    '<li>' +
                    '<a class="btn" data-wysihtml5-command="browser">' +
                    '<i class="icon-folder-open"></i>' +
                    '</a>' +
                    '</li>'
            }
        });
    };

}(jQuery));
