odoo.define('website_country_selector.country_selector', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');

    publicWidget.registry.CountrySelector = publicWidget.Widget.extend({
        selector: '#wrapwrap',
        events: {
            'change #country-selector': '_onCountryChange',
            'click #country-selector-save': '_onSaveClick',
        },

        start: function () {
            this.$modal = $('#country-selector-dialog');
            this.$modal.modal('show'); // Show dialog on page load
            return this._super.apply(this, arguments);
        },

        _onCountryChange: function (ev) {
            var $select = $(ev.currentTarget);
            var countryCode = $select.find('option:selected').data('code');
            var $flagImage = this.$modal.find('#flag-image');
            if (countryCode) {
                $flagImage.attr('src', '/web/image/res.country/' + $select.val() + '/image');
                $flagImage.show();
            } else {
                $flagImage.hide();
            }
        },

        _onSaveClick: function () {
            var self = this;
            var countryId = this.$modal.find('#country-selector').val();
            if (countryId) {
                this._rpc({
                    route: '/website/set_country_pricelist',
                    params: { country_id: countryId },
                }).then(function (result) {
                    if (result.success) {
                        window.location.reload(); // Reload to apply pricelist
                    } else {
                        alert('No pricelist found for this country.');
                    }
                });
            }
        },
    });

    return publicWidget.registry.CountrySelector;
});