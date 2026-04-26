#pragma once

#include "esphome/components/select/select.h"
#include "esphome/core/component.h"

namespace esphome
{
    namespace ykh531e
    {

        // Forward declaration — avoids circular include with ykh531e.h
        class YKH531EClimate;

        class YKH531ETimerSelect : public select::Select, public Component
        {
        public:
            void set_parent(YKH531EClimate *parent) { this->parent_ = parent; }

            float get_setup_priority() const override { return setup_priority::DATA; }

        protected:
            void control(const std::string &value) override;

            YKH531EClimate *parent_{nullptr};
        };

    } // namespace ykh531e
} // namespace esphome