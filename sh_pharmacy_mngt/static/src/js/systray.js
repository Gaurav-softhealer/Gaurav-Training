/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";

class CustomSystray extends Component {
    setup() {
        // You can use setup for logic or hooks
    }

    onClick() {
        // Your custom logic here
        alert("Custom icon clicked!");
    }
}

CustomSystray.template = "music_academy.CustomSystrayTemplate";

// Register your systray item
registry.category("systray").add("music_academy.CustomSystray", {
    Component: CustomSystray,
});
