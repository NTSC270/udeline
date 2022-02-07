import pyfiglet as fig
import math, markup_ansi, commands, re

async def run_command(discord, message, args, client, opt):
    args.pop(0)

    if len(args) < 1:
        return await commands.run_command("help", discord, message, ["u>help", "ascii"], client, [])

    fontt = "stop"
    color = "clear"
    colors = ["red", "pink", "green", "yellow", "blue", "aqua", "white", "dark_fill", "red_fill", "discord_fill", "clear", "washed_fill", "grey_fill"]

    allfonts = ['1943____', 'dcs_bfmo', 'letterw3', 'small', '3-d', 'd_dragon', 'letter_w', 'sm______', '3x5', 'decimal', 'lexible_', 'smisome1', '4x4_offr', 'deep_str', 'linux', 'smkeyboard', '5lineoblique', 'defleppard', 'lockergnome', 'smscript', '5x7', 'demo_1__', 'lower', 'smshadow', '5x8', 'demo_2__', 'mad_nurs', 'smslant', '64f1____', 'demo_m__', 'madrid', 'smtengwar', '6x10', 'devilish', 'magic_ma', 'space_op', '6x9', 'diamond', 'marquee', 'spc_demo', 'acrobatic', 'digital', 'master_o', 'speed', 'advenger', 'doh', 'maxfour', 'stacey', 'alligator2', 'doom', 'mayhem_d', 'stampatello', 'alligator', 'dotmatrix', 'mcg_____', 'standard', 'alphabet', 'double', 'mig_ally', 'star_war', 'aquaplan', 'drpepper', 'mike', 'starwars', 'arrows', 'druid___', 'mini', 'stealth_', 'asc_____', 'dwhistled', 'mirror', 'stellar', 'ascii___', 'ebbs_1__', 'mnemonic', 'stencil1', 'assalt_m', 'ebbs_2__', 'modern__', 'stencil2', 'asslt__m', 'eca_____', 'morse', 'stop', 'atc_____', 'e__fist_', 'moscow', 'straight', 'atc_gran', 'eftichess', 'mshebrew210', 'street_s', 'avatar', 'eftifont', 'nancyj-fancy', 'subteran', 'a_zooloo', 'eftipiti', 'nancyj', 'super_te', 'banner3-D', 'eftirobot', 'nancyj-underlined', 'tanja', 'banner3', 'eftitalic', 'new_asci', 'tav1____', 'banner4', 'eftiwall', 'nfi1____', 'taxi____', 'banner', 'eftiwater', 'nipples', 'tec1____', 'barbwire', 'epic', 'notie_ca', 'tec_7000', 'basic', 'etcrvs__', 'npn_____', 'tecrvs__', 'battle_s', 'f15_____', 'ntgreek', 'tengwar', 'battlesh', 'faces_of', 'null', 'term', 'baz__bil', 'fairligh', 'nvscript', 'thick', 'beer_pub', 'fair_mea', 'o8', 'thin', 'bell', 'fantasy_', 'octal', 'threepoint', 'bigchief', 'fbr12___', 'odel_lak', 'ticks', 'big', 'fbr1____', 'ogre', 'ticksslant', 'binary', 'fbr2____', 'ok_beer_', 'tiles', 'block', 'fbr_stri', 'os2', 'times', 'b_m__200', 'fbr_tilt', 'outrun__', 'timesofl', 'briteb', 'fender', 'pacos_pe', 'tinker-toy', 'britebi', 'finalass', 'panther_', 'ti_pan__', 'brite', 'fireing_', 'pawn_ins', 't__of_ap', 'britei', 'flyn_sh', 'pawp', 'tomahawk', 'broadway', 'fourtops', 'peaks', 'tombstone', 'bubble_b', 'fp1_____', 'pebbles', 'top_duck', 'bubble', 'fp2_____', 'pepper', 'trashman', 'bubble__', 'fraktur', 'phonix__', 'trek', 'bulbhead', 'funky_dr', 'platoon2', 'triad_st', 'c1______', 'future_1', 'platoon_', 'ts1_____', 'c2______', 'future_2', 'pod_____', 'tsalagi', 'calgphy2', 'future_3', 'poison', 'tsm_____', 'caligraphy', 'future_4', 'p_s_h_m_', 'tsn_base', 'c_ascii_', 'future_5', 'p_skateb', 'ttyb', 'catwalk', 'future_6', 'puffy', 'tty', 'caus_in_', 'future_7', '__pycache__', 'tubular', 'c_consen', 'future_8', 'pyramid', 'twin_cob', 'char1___', 'fuzzy', 'r2-d2___', 'twopoint', 'char2___', 'gauntlet', 'rad_____', 'type_set', 'char3___', 'ghost_bo', 'radical_', 'ucf_fan_', 'char4___', 'goofy', 'rad_phan', 'ugalympi', 'charact1', 'gothic', 'rainbow_', 'unarmed_', 'charact2', 'gothic__', 'rally_s2', 'univers', 'charact3', 'graceful', 'rally_sp', 'upper', 'charact4', 'gradient', 'rampage_', 'usaflag', 'charact5', 'graffiti', 'rastan__', 'usa_____', 'charact6', 'grand_pr', 'raw_recu', 'usa_pq__', 'characte', 'greek', 'rci_____', 'utopiab', 'charset_', 'green_be', 'rectangles', 'utopiabi', 'chartr', 'hades___', 'relief2', 'utopia', 'chartri', 'heavy_me', 'relief', 'utopiai', 'chunky', 'helvb', 'rev', 'vortron_', 'clb6x10', 'helvbi', "'ripper!_'", 'war_of_w', 'clb8x10', 'helv', 'road_rai', 'wavy', 'clb8x8', 'helvi', 'rockbox_', 'weird', 'cli8x8', 'heroboti', 'rok_____', 'whimsy', 'clr4x6', 'hex', 'roman', 'xbriteb', 'clr5x10', 'high_noo', 'roman___', 'xbritebi', 'clr5x6', 'hills___', 'rot13', 'xbrite', 'clr5x8', 'hollywood', 'rot13', 'xbritei', 'clr6x10', 'home_pak', 'rounded', 'xchartr', 'clr6x6', 'house_of', 'rowancap', 'xchartri', 'clr6x8', 'hypa_bal', 'rozzo', 'xcourb', 'clr7x10', 'hyper___', 'runic', 'xcourbi', 'clr7x8', 'inc_raw_', 'runyc', 'xcour', 'clr8x10', '__init__', 'sansb', 'xcouri', 'clr8x8', 'invita', 'sansbi', 'xhelvb', 'coil_cop', 'isometric1', 'sans', 'xhelvbi', 'coinstak', 'isometric2', 'sansi', 'xhelv', 'colossal', 'isometric3', 'sblood', 'xhelvi', 'computer', 'isometric4', 'sbookb', 'xsansb', 'com_sen_', 'italic', 'sbookbi', 'xsansbi', 'contessa', 'italics_', 'sbook', 'xsans', 'contrast', 'ivrit', 'sbooki', 'xsansi', 'convoy__', 'jazmine', 'script', 'xsbookb', 'cosmic', 'jerusalem', 'script__', 'xsbookbi', 'cosmike', 'joust___', 'serifcap', 'xsbook', 'courb', 'katakana', 'shadow', 'xsbooki', 'courbi', 'kban', 'shimrod', 'xtimes', 'cour', 'kgames_i', 'short', 'xttyb', 'couri', 'kik_star', 'skateord', 'xtty', 'crawford', 'krak_out', 'skateroc', 'yie-ar__', 'cricket', 'larry3d', 'skate_ro', 'yie_ar_k', 'cursive', 'lazy_jon', 'sketch_s', 'zig_zag_', 'cyberlarge', 'lcd', 'slant', 'zone7___', 'cybermedium', 'lean', 'slide', 'z-pilot_', 'cybersmall', 'letters', 'slscript']
    
    for x in range(len(opt)):
        opt[x] = opt[x].split("=")
        if opt[x][0] == "font":
            fontt = re.sub("\n.*$", "", opt[x][1])
        if opt[x][0] == "color":
            color = re.sub("\n.*$", "", opt[x][1])
    if not fontt.strip() in allfonts:
        print(fontt.strip())
        await message.reply("invalid font, available fonts can be found here https://pastebin.com/SdPVt65W")
        return
    if not color.strip() in colors:
        await message.reply("invalid color, available colors are\n`"+", ".join(colors)+"`")
        return

    f = fig.Figlet(font=fontt.strip())
    if color != "clear":
        output = markup_ansi.getc(color, "0")+f.renderText(" ".join(args)).replace("`", "\0`")
        await message.reply((">>> ```ansi\n"+output[0:1981]+"```"))
    else:
        output = f.renderText(" ".join(args)).replace("`", "\0`")
        await message.reply((">>> ```\n"+output[0:1988]+"```"))

    
