# Copyright (c) 2021 rdbende <rdbende@gmail.com>

# Azure theme is a beautiful modern ttk theme inspired by Microsoft's fluent design.

package require Tk 8.6

namespace eval ttk::theme::azure-dark {

    variable version 1.3
    package provide ttk::theme::azure-dark $version
    variable colors
    array set colors {
        -fg             "#ffffff"
        -bg             "#1f1f1f"
        -disabledfg     "#ffffff"
        -disabledbg     "#737373"
        -selectfg       "#ffffff"
        -selectbg       "#007fff"
    }

    proc LoadImages {imgdir} {
        variable I
        foreach file [glob -directory $imgdir *.gif] {
            set img [file tail [file rootname $file]]
            set I($img) [image create photo -file $file -format gif]
        }
    }

    LoadImages [file join [file dirname [info script]] azure-dark]

    # Settings
    ttk::style theme create azure-dark -parent default -settings {
        ttk::style configure . \
            -background $colors(-bg) \
            -foreground $colors(-fg) \
            -troughcolor $colors(-bg) \
            -focuscolor $colors(-selectbg) \
            -selectbackground $colors(-selectbg) \
            -selectforeground $colors(-selectfg) \
            -insertcolor $colors(-fg) \
            -insertwidth 1 \
            -fieldbackground $colors(-selectbg) \
            -font "Calibri 11" \
            -borderwidth 1 \
            -relief flat

        ttk::style map . -foreground [list disabled $colors(-disabledfg)]

        tk_setPalette background [ttk::style lookup . -background] \
            foreground [ttk::style lookup . -foreground] \
            highlightColor [ttk::style lookup . -focuscolor] \
            selectBackground [ttk::style lookup . -selectbackground] \
            selectForeground [ttk::style lookup . -selectforeground] \
            activeBackground [ttk::style lookup . -selectbackground] \
            activeForeground [ttk::style lookup . -selectforeground]
        option add *font [ttk::style lookup . -font]



        ttk::style layout lockSwitch {
            lockSwitch.button -children {
                lockSwitch.padding -children {
                    lockSwitch.indicator -side left
                    lockSwitch.label -side right -expand true
                }
            }
        }

        ttk::style layout currencySwitch {
            currencySwitch.button -children {
                currencySwitch.padding -children {
                    currencySwitch.indicator -side left
                    currencySwitch.label -side right -expand true
                }
            }
        }

        # ComboboxLong-1
        ttk::style layout ComboboxLong1 {
            ComboboxLong1.field -sticky nswe -children {
                ComboboxLong1.padding -expand true -sticky nswe -children {
                    ComboboxLong1.textarea -sticky nswe
                }
            }
            ComboboxLong1.button -side right -sticky ns -children {
                ComboboxLong1.arrow -sticky nsew
            }
        }

        # ComboboxLong-2
        ttk::style layout ComboboxLong2 {
            ComboboxLong2.field -sticky nswe -children {
                ComboboxLong2.padding -expand true -sticky nswe -children {
                    ComboboxLong2.textarea -sticky nswe
                }
            }
            ComboboxLong2.button -side right -sticky ns -children {
                ComboboxLong2.arrow -sticky nsew
            }
        }

        # ComboboxShort
        ttk::style layout ComboboxShort {
            ComboboxShort.field -sticky nswe -children {
                ComboboxShort.padding -expand true -sticky nswe -children {
                    ComboboxShort.textarea -sticky nswe
                }
            }
            ComboboxShort.button -side right -sticky ns -children {
                ComboboxShort.arrow -sticky nsew
            }
        }

        # Entry Long - 1
        ttk::style layout EntryLong1 {
            EntryLong1.field -sticky nswe -children {
                EntryLong1.padding -expand true -sticky nswe -children {
                    EntryLong1.textarea -sticky nswe
                }
            }
        }

        # Entry Long - 2
        ttk::style layout EntryLong2 {
            EntryLong2.field -sticky nswe -children {
                EntryLong2.padding -expand true -sticky nswe -children {
                    EntryLong2.textarea -sticky nswe
                }
            }
        }

        # Entry Short - 1
        ttk::style layout EntryShort1 {
            EntryShort1.field -sticky nswe -children {
                EntryShort1.padding -expand true -sticky nswe -children {
                    EntryShort1.textarea -sticky nswe
                }
            }
        }

        # Entry Short - 2
        ttk::style layout EntryShort2 {
            EntryShort2.field -sticky nswe -children {
                EntryShort2.padding -expand true -sticky nswe -children {
                    EntryShort2.textarea -sticky nswe
                }
            }
        }

        # Entry Middle
        ttk::style layout EntryMiddle {
            EntryMiddle.field -sticky nswe -children {
                EntryMiddle.padding -expand true -sticky nswe -children {
                    EntryMiddle.textarea -sticky nswe
                }
            }
        }


        ttk::style layout Horizontal.TSeparator {
            Horizontal.separator -sticky nswe
        }

        ttk::style layout Vertical.TSeparator {
            Vertical.separator -sticky nswe
        }


        ttk::style layout Vertical.TScrollbar {
            Vertical.Scrollbar.trough -sticky ns -children {
                Vertical.Scrollbar.thumb -expand true
            }
        }

        ttk::style layout Horizontal.TScrollbar {
            Horizontal.Scrollbar.trough -sticky ew -children {
                Horizontal.Scrollbar.thumb -expand true
            }
        }



        # Elements


        # lockSwitch
        ttk::style element create lockSwitch.indicator image \
            [list $I(lockSwitch-off-basic) \
                {selected disabled} $I(lockSwitch-on-basic) \
                disabled $I(lockSwitch-off-basic) \
                {pressed selected} $I(lockSwitch-on-hover) \
                {active selected} $I(lockSwitch-on-hover) \
                selected $I(lockSwitch-on-accent) \
                {pressed !selected} $I(lockSwitch-off-hover) \
                active $I(lockSwitch-off-hover) \
            ] -width 46 -sticky w

        # currencySwitch
        ttk::style element create currencySwitch.indicator image \
            [list $I(currencySwitch-off-basic) \
                {selected disabled} $I(currencySwitch-on-basic) \
                disabled $I(currencySwitch-off-basic) \
                {pressed selected} $I(currencySwitch-on-hover) \
                {active selected} $I(currencySwitch-on-hover) \
                selected $I(currencySwitch-on-accent) \
                {pressed !selected} $I(currencySwitch-off-hover) \
                active $I(currencySwitch-off-hover) \
            ] -width 46 -sticky w

        # Entry Long - 1
        ttk::style element create EntryLong1.field \
            image [list $I(entry-long-1-basic) \
                {focus hover} $I(entry-long-1-accent) \
                invalid $I(box-invalid) \
                disabled $I(entry-long-1-basic) \
                focus $I(entry-long-1-accent) \
                hover $I(entry-long-1-hover) \
            ] -border 0 -padding {15 1} -sticky news

        # Entry Long - 2
        ttk::style element create EntryLong2.field \
            image [list $I(entry-long-2-basic) \
                {focus hover} $I(entry-long-2-accent) \
                invalid $I(box-invalid) \
                disabled $I(entry-long-2-basic) \
                focus $I(entry-long-2-accent) \
                hover $I(entry-long-2-hover) \
            ] -border 0 -padding {15 1} -sticky news

        # Entry Short - 1
        ttk::style element create EntryShort1.field \
            image [list $I(entry-short-1-basic) \
                {focus hover} $I(entry-short-1-accent) \
                invalid $I(box-invalid) \
                disabled $I(entry-short-1-basic) \
                focus $I(entry-short-1-accent) \
                hover $I(entry-short-1-hover) \
            ] -border 0 -border 0 -padding {15 1} -sticky news

        # Entry Short - 2
        ttk::style element create EntryShort2.field \
            image [list $I(entry-short-2-basic) \
                {focus hover} $I(entry-short-2-accent) \
                invalid $I(box-invalid) \
                disabled $I(entry-short-2-basic) \
                focus $I(entry-short-2-accent) \
                hover $I(entry-short-2-hover) \
            ] -border 0 -border 0 -padding {15 1} -sticky news

        # Entry Middle
        ttk::style element create EntryMiddle.field \
            image [list $I(entry-middle-basic) \
                {focus hover} $I(entry-middle-accent) \
                invalid $I(box-invalid) \
                disabled $I(entry-middle-basic) \
                focus $I(entry-middle-accent) \
                hover $I(entry-middle-hover) \
            ] -border 0 -border 0 -padding {15 1} -sticky news

        # Combobox Long - 1
        ttk::style map ComboboxLong1 -selectbackground [list \
            {!focus} $colors(-selectbg) \
            {readonly hover} $colors(-selectbg) \
            {readonly focus} $colors(-selectbg) \
        ]
            
        ttk::style map ComboboxLong1 -selectforeground [list \
            {!focus} $colors(-selectfg) \
            {readonly hover} $colors(-selectfg) \
            {readonly focus} $colors(-selectfg) \
        ]

        ttk::style element create ComboboxLong1.field \
            image [list $I(combo-long-1-basic) \
                {readonly disabled} $I(rect-basic) \
                {readonly pressed} $I(rect-basic) \
                {readonly focus hover} $I(button-hover) \
                {readonly focus} $I(button-hover) \
                {readonly hover} $I(button-hover) \
                {focus hover} $I(combo-long-1-accent) \
                readonly $I(rect-basic) \
                invalid $I(box-invalid) \
                disabled $I(combo-long-1-basic) \
                focus $I(combo-long-1-accent) \
                hover $I(combo-long-1-hover) \
            ] -border 5 -padding {15 1}
            
        ttk::style element create ComboboxLong1.button \
            image [list $I(combo-button-basic) \
                 {!readonly focus} $I(combo-button-focus) \
                 {readonly focus} $I(combo-button-hover) \
                 {readonly hover} $I(combo-button-hover) \
                 {hover} $I(combo-button-hover)
            ] -border 5 -padding {2 6 6 6}

        ttk::style element create ComboboxLong1.arrow image $I(down) \
            -width 15 -sticky w 

        # Combobox Long - 2
        ttk::style map ComboboxLong2 -selectbackground [list \
            {!focus} $colors(-selectbg) \
            {readonly hover} $colors(-selectbg) \
            {readonly focus} $colors(-selectbg) \
        ]
            
        ttk::style map ComboboxLong2 -selectforeground [list \
            {!focus} $colors(-selectfg) \
            {readonly hover} $colors(-selectfg) \
            {readonly focus} $colors(-selectfg) \
        ]

        ttk::style element create ComboboxLong2.field \
            image [list $I(combo-long-2-basic) \
                {readonly disabled} $I(rect-basic) \
                {readonly pressed} $I(rect-basic) \
                {readonly focus hover} $I(button-hover) \
                {readonly focus} $I(button-hover) \
                {readonly hover} $I(button-hover) \
                {focus hover} $I(combo-long-2-accent) \
                readonly $I(rect-basic) \
                invalid $I(box-invalid) \
                disabled $I(combo-long-2-basic) \
                focus $I(combo-long-2-accent) \
                hover $I(combo-long-2-hover) \
            ] -border 5 -padding {15 1}
            
        ttk::style element create ComboboxLong2.button \
            image [list $I(combo-button-basic) \
                 {!readonly focus} $I(combo-button-focus) \
                 {readonly focus} $I(combo-button-hover) \
                 {readonly hover} $I(combo-button-hover) \
                 {hover} $I(combo-button-hover)
            ] -border 5 -padding {2 6 6 6}

        ttk::style element create ComboboxLong2.arrow image $I(down) \
            -width 15 -sticky w 


        # ComboboxShort
        ttk::style map ComboboxShort -selectbackground [list \
            {!focus} $colors(-selectbg) \
            {readonly hover} $colors(-selectbg) \
            {readonly focus} $colors(-selectbg) \
        ]
            
        ttk::style map ComboboxShort -selectforeground [list \
            {!focus} $colors(-selectfg) \
            {readonly hover} $colors(-selectfg) \
            {readonly focus} $colors(-selectfg) \
        ]

        ttk::style element create ComboboxShort.field \
            image [list $I(combo-short-basic) \
                {readonly disabled} $I(rect-basic) \
                {readonly pressed} $I(rect-basic) \
                {readonly focus hover} $I(button-hover) \
                {readonly focus} $I(button-hover) \
                {readonly hover} $I(button-hover) \
                {focus hover} $I(combo-short-accent) \
                readonly $I(rect-basic) \
                invalid $I(box-invalid) \
                disabled $I(combo-short-basic) \
                focus $I(combo-short-accent) \
                hover $I(combo-short-hover) \
            ] -border 5 -padding {15 1 30 0}
            
        ttk::style element create ComboboxShort.button \
            image [list $I(combo-button-basic) \
                 {!readonly focus} $I(combo-button-focus) \
                 {readonly focus} $I(combo-button-hover) \
                 {readonly hover} $I(combo-button-hover) \
                 {hover} $I(combo-button-hover) \
                 {focus} $I(combo-button-focus)
            ] -border 5 -padding {2 6 6 6}

        ttk::style element create ComboboxShort.arrow image $I(down) \
            -width 15 -sticky w 


        # Separator
        ttk::style element create Horizontal.separator image $I(separator)

        ttk::style element create Vertical.separator image $I(separator)
        
        # Scrollbar
        ttk::style element create Horizontal.Scrollbar.trough image $I(hor-basic) \
            -sticky ew

        ttk::style element create Horizontal.Scrollbar.thumb \
             image [list $I(hor-accent) \
                disabled $I(hor-basic) \
                pressed $I(hor-hover) \
                active $I(hor-hover) \
            ] -sticky ew

        ttk::style element create Vertical.Scrollbar.trough image $I(vert-basic) \
            -sticky ns

        ttk::style element create Vertical.Scrollbar.thumb \
            image [list $I(vert-basic) \
                disabled  $I(vert-basic) \
                pressed $I(vert-basic) \
                active $I(vert-basic) \
            ] -sticky ns



        # Sashes
        #ttk::style map TPanedwindow \
        #    -background [list hover $colors(-bg)]
    }
}
