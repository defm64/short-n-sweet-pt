init offset = 999
screen navigation():
    fixed:
        style_prefix "navigation"
        spacing gui.navigation_spacing
        if main_menu:
            imagebutton auto "gui/mm_start_%s.png" xpos 846 ypos 835 action Start() hover_sound "pl2.mp3" activate_sound "pl1.mp3"
            imagebutton auto "gui/mm_load_%s.png" xpos 846 ypos 946 action ShowMenu("load") hover_sound "pl2.mp3" activate_sound "pl1.mp3"
            imagebutton auto "gui/mm_gallery_%s.png" xpos 38 ypos 835 action ShowMenu("Gallery") hover_sound "pl2.mp3" activate_sound "pl1.mp3"
            imagebutton auto "gui/mm_sexpansions_%s.png" xpos 38 ypos 946 action ShowMenu("Sexphub") hover_sound "pl2.mp3" activate_sound "pl1.mp3"
            imagebutton auto "gui/mm_settings_%s.png" xpos 1558 ypos 946 action ShowMenu("preferences") hover_sound "pl2.mp3" activate_sound "pl1.mp3"
            imagebutton auto "gui/mm_faq_%s.png" xpos 1421 ypos 835 action ShowMenu("faq") hover_sound "pl2.mp3" activate_sound "pl1.mp3"
            imagebutton auto "gui/mm_quit_%s.png" xpos 1696 ypos 835 action Quit(confirm=not main_menu) hover_sound "pl2.mp3" activate_sound "pl1.mp3"
            imagebutton auto "gui/m_pbutton_%s.png" xpos 1811 ypos 692 action OpenURL("www.patreon.com/pureharem") hover_sound "pl2.mp3" activate_sound "pl1.mp3"
            imagebutton auto "defm64/defm64_%s.png" xpos 0 ypos 692 action OpenURL("https://allmylinks.com/defm64") hover_sound "pl2.mp3" activate_sound "pl1.mp3"
        else:
            vbox:
                xpos gui.navigation_xpos
                yalign 0.5
                textbutton _("History") action ShowMenu("history")
                textbutton _("Save") action ShowMenu("save")
                textbutton _("Load") action ShowMenu("load")
                textbutton _("Preferences") action ShowMenu("preferences")
                textbutton _("Gallery") action ShowMenu('Gallery')
                textbutton _("About") action ShowMenu("about")
                textbutton _("Help") action ShowMenu("help")
                if _in_replay:
                    textbutton _("End Replay") action EndReplay(confirm=True)
                elif not main_menu:
                    textbutton _("Main Menu") action MainMenu()
                textbutton _("Quit") action Quit(confirm=not main_menu)
screen about():
    tag menu
    use game_menu(_("About"), scroll="viewport"):
        style_prefix "about"
        vbox:
            label "[config.name!t]"
            text _("Version [config.version!t]\n")
            if gui.about:
                text "[gui.about!t]\n"
            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
            text _("\nPortuguese translation by {a=https://allmylinks.com/defm64}defm64{/a}.\nLicensed under {a=https://creativecommons.org/licenses/by-nc-sa/4.0/}CC BY-NC-SA 4.0{/a}.")
screen preferences():
    tag menu
    add "gui/game_menu.png"
    use game_menu(_("Preferences"), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True
                vbox:
                    style_prefix "radio"
                    label _("Language")
                    textbutton "English" action Language(None)
                    textbutton "Português" action Language("portuguese")
                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
            null height (4 * gui.pref_spacing)
            hbox:
                vbox:
                    style_prefix "slider"
                    $ pdBO = int(persistent.dialogueBoxOpacity*100)
                    label _("Dialogue box opacity")
                    bar value FieldValue(persistent, "dialogueBoxOpacity", range=1.0, style="slider")
            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:
                    label _("Text Speed")
                    bar value Preference("text speed")
                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")
                vbox:
                    if config.has_music:
                        label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")
                    if config.has_sound:
                        label _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)
                    if config.has_voice:
                        label _("Voice Volume")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)
                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
screen disclaimer:
    tag menu
    add gui.main_menu_background alpha 0.5 blur 15.0
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 50
        xsize 1920
        style_prefix "choice"
        hbox:
            xalign 0.5
            vbox:
                xalign 0.5
                style_prefix "radio"
                label _("Language") xalign 0.5
                textbutton "English" action Language(None) xalign 0.5
                textbutton "Português" action Language("portuguese") xalign 0.5
        textbutton _("I am 18 or older.") action Return() xalign 0.5
        textbutton _("I am under 18.") action Quit() xalign 0.5
