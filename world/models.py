
# Django imports
from django.core.urlresolvers import reverse
from django.utils import translation
from django.db import models


class Continent(models.Model):
    """
    Data model for world continents.
    """
    name_ar             = models.CharField("name (ar)", max_length = 200, blank = True)
    name_bg             = models.CharField("name (bg)", max_length = 200, blank = True)
    name_bn             = models.CharField("name (bn)", max_length = 200, blank = True)
    name_ca             = models.CharField("name (ca)", max_length = 200, blank = True)
    name_cs             = models.CharField("name (cs)", max_length = 200, blank = True)
    name_cy             = models.CharField("name (cy)", max_length = 200, blank = True)
    name_da             = models.CharField("name (da)", max_length = 200, blank = True)
    name_de             = models.CharField("name (de)", max_length = 200, blank = True)
    name_el             = models.CharField("name (el)", max_length = 200, blank = True)
    name_en             = models.CharField("name (en)", max_length = 200, unique = True)
    name_es             = models.CharField("name (es)", max_length = 200, blank = True)
    name_es_AR          = models.CharField("name (es_AR)", max_length = 200, blank = True)
    name_et             = models.CharField("name (et)", max_length = 200, blank = True)
    name_eu             = models.CharField("name (eu)", max_length = 200, blank = True)
    name_fa             = models.CharField("name (fa)", max_length = 200, blank = True)
    name_fi             = models.CharField("name (fi)", max_length = 200, blank = True)
    name_fr             = models.CharField("name (fr)", max_length = 200, blank = True)
    name_ga             = models.CharField("name (ga)", max_length = 200, blank = True)
    name_gl             = models.CharField("name (gl)", max_length = 200, blank = True)
    name_he             = models.CharField("name (he)", max_length = 200, blank = True)
    name_hi             = models.CharField("name (hi)", max_length = 200, blank = True)
    name_hr             = models.CharField("name (hr)", max_length = 200, blank = True)
    name_hu             = models.CharField("name (hu)", max_length = 200, blank = True)
    name_is             = models.CharField("name (is)", max_length = 200, blank = True)
    name_it             = models.CharField("name (it)", max_length = 200, blank = True)
    name_ja             = models.CharField("name (ja)", max_length = 200, blank = True)
    name_ka             = models.CharField("name (ka)", max_length = 200, blank = True)
    name_km             = models.CharField("name (km)", max_length = 200, blank = True)
    name_kn             = models.CharField("name (kn)", max_length = 200, blank = True)
    name_ko             = models.CharField("name (ko)", max_length = 200, blank = True)
    name_lt             = models.CharField("name (lt)", max_length = 200, blank = True)
    name_lv             = models.CharField("name (lv)", max_length = 200, blank = True)
    name_mk             = models.CharField("name (mk)", max_length = 200, blank = True)
    name_nl             = models.CharField("name (nl)", max_length = 200, blank = True)
    name_no             = models.CharField("name (no)", max_length = 200, blank = True)
    name_pl             = models.CharField("name (pl)", max_length = 200, blank = True)
    name_pt             = models.CharField("name (pt)", max_length = 200, blank = True)
    name_pt_BR          = models.CharField("name (pt_BR)", max_length = 200, blank = True)
    name_ro             = models.CharField("name (ro)", max_length = 200, blank = True)
    name_ru             = models.CharField("name (ru)", max_length = 200, blank = True)
    name_sk             = models.CharField("name (sk)", max_length = 200, blank = True)
    name_sl             = models.CharField("name (sl)", max_length = 200, blank = True)
    name_sr             = models.CharField("name (sr)", max_length = 200, blank = True)
    name_sr_Latn        = models.CharField("name (sr_Latn)", max_length = 200, blank = True)
    name_sv             = models.CharField("name (sv)", max_length = 200, blank = True)
    name_ta             = models.CharField("name (ta)", max_length = 200, blank = True)
    name_te             = models.CharField("name (te)", max_length = 200, blank = True)
    name_th             = models.CharField("name (th)", max_length = 200, blank = True)
    name_tr             = models.CharField("name (tr)", max_length = 200, blank = True)
    name_uk             = models.CharField("name (uk)", max_length = 200, blank = True)
    name_zh_CN          = models.CharField("name (zh_CN)", max_length = 200, blank = True)
    name_zh_TW          = models.CharField("name (zh_TW)", max_length = 200, blank = True)
    slug                = models.SlugField(max_length = 200, unique = True,
                                help_text = "Automatically created from the English name")

    class Meta:
        ordering             = ('name_en', )
        verbose_name         = "continent"
        verbose_name_plural  = "continents"

    def __unicode__(self):
        try:
            name_field = "name_%s" % translation.get_language()
            value = getattr(self, name_field)
            if value:
                return u'%s' % value
            else:
                return self.name_en
        except:
            return self.name_en


class Region(models.Model):
    """
    Data model for world regions.
    """
    continents          = models.ManyToManyField(Continent)
    name_ar             = models.CharField("name (ar)", max_length = 200, blank = True)
    name_bg             = models.CharField("name (bg)", max_length = 200, blank = True)
    name_bn             = models.CharField("name (bn)", max_length = 200, blank = True)
    name_ca             = models.CharField("name (ca)", max_length = 200, blank = True)
    name_cs             = models.CharField("name (cs)", max_length = 200, blank = True)
    name_cy             = models.CharField("name (cy)", max_length = 200, blank = True)
    name_da             = models.CharField("name (da)", max_length = 200, blank = True)
    name_de             = models.CharField("name (de)", max_length = 200, blank = True)
    name_el             = models.CharField("name (el)", max_length = 200, blank = True)
    name_en             = models.CharField("name (en)", max_length = 200, unique = True)
    name_es             = models.CharField("name (es)", max_length = 200, blank = True)
    name_es_AR          = models.CharField("name (es_AR)", max_length = 200, blank = True)
    name_et             = models.CharField("name (et)", max_length = 200, blank = True)
    name_eu             = models.CharField("name (eu)", max_length = 200, blank = True)
    name_fa             = models.CharField("name (fa)", max_length = 200, blank = True)
    name_fi             = models.CharField("name (fi)", max_length = 200, blank = True)
    name_fr             = models.CharField("name (fr)", max_length = 200, blank = True)
    name_ga             = models.CharField("name (ga)", max_length = 200, blank = True)
    name_gl             = models.CharField("name (gl)", max_length = 200, blank = True)
    name_he             = models.CharField("name (he)", max_length = 200, blank = True)
    name_hi             = models.CharField("name (hi)", max_length = 200, blank = True)
    name_hr             = models.CharField("name (hr)", max_length = 200, blank = True)
    name_hu             = models.CharField("name (hu)", max_length = 200, blank = True)
    name_is             = models.CharField("name (is)", max_length = 200, blank = True)
    name_it             = models.CharField("name (it)", max_length = 200, blank = True)
    name_ja             = models.CharField("name (ja)", max_length = 200, blank = True)
    name_ka             = models.CharField("name (ka)", max_length = 200, blank = True)
    name_km             = models.CharField("name (km)", max_length = 200, blank = True)
    name_kn             = models.CharField("name (kn)", max_length = 200, blank = True)
    name_ko             = models.CharField("name (ko)", max_length = 200, blank = True)
    name_lt             = models.CharField("name (lt)", max_length = 200, blank = True)
    name_lv             = models.CharField("name (lv)", max_length = 200, blank = True)
    name_mk             = models.CharField("name (mk)", max_length = 200, blank = True)
    name_nl             = models.CharField("name (nl)", max_length = 200, blank = True)
    name_no             = models.CharField("name (no)", max_length = 200, blank = True)
    name_pl             = models.CharField("name (pl)", max_length = 200, blank = True)
    name_pt             = models.CharField("name (pt)", max_length = 200, blank = True)
    name_pt_BR          = models.CharField("name (pt_BR)", max_length = 200, blank = True)
    name_ro             = models.CharField("name (ro)", max_length = 200, blank = True)
    name_ru             = models.CharField("name (ru)", max_length = 200, blank = True)
    name_sk             = models.CharField("name (sk)", max_length = 200, blank = True)
    name_sl             = models.CharField("name (sl)", max_length = 200, blank = True)
    name_sr             = models.CharField("name (sr)", max_length = 200, blank = True)
    name_sr_Latn        = models.CharField("name (sr_Latn)", max_length = 200, blank = True)
    name_sv             = models.CharField("name (sv)", max_length = 200, blank = True)
    name_ta             = models.CharField("name (ta)", max_length = 200, blank = True)
    name_te             = models.CharField("name (te)", max_length = 200, blank = True)
    name_th             = models.CharField("name (th)", max_length = 200, blank = True)
    name_tr             = models.CharField("name (tr)", max_length = 200, blank = True)
    name_uk             = models.CharField("name (uk)", max_length = 200, blank = True)
    name_zh_CN          = models.CharField("name (zh_CN)", max_length = 200, blank = True)
    name_zh_TW          = models.CharField("name (zh_TW)", max_length = 200, blank = True)
    slug                = models.SlugField(max_length = 200, unique = True,
                                help_text = "Automatically created from the English name")

    class Meta:
        ordering             = ('name_en', )
        verbose_name         = "region"
        verbose_name_plural  = "regions"

    def __unicode__(self):
        try:
            name_field = "name_%s" % translation.get_language()
            value = getattr(self, name_field)
            if value:
                return u'%s' % value
            else:
                return self.name_en
        except:
            return self.name_en


class Country(models.Model):
    """
    Data model for world counties.
    """
    iso_3166_alpha2     = models.CharField("iso-3166 alpha2", max_length = 2)
    iso_3166_alpha3     = models.CharField("iso-3166 alpha3", max_length = 3)
    iso_3166_numeric    = models.PositiveSmallIntegerField("iso-3166 numberic")
    regions             = models.ManyToManyField(Region)
    name_ar             = models.CharField("name (ar)", max_length = 200, blank = True)
    name_bg             = models.CharField("name (bg)", max_length = 200, blank = True)
    name_bn             = models.CharField("name (bn)", max_length = 200, blank = True)
    name_ca             = models.CharField("name (ca)", max_length = 200, blank = True)
    name_cs             = models.CharField("name (cs)", max_length = 200, blank = True)
    name_cy             = models.CharField("name (cy)", max_length = 200, blank = True)
    name_da             = models.CharField("name (da)", max_length = 200, blank = True)
    name_de             = models.CharField("name (de)", max_length = 200, blank = True)
    name_el             = models.CharField("name (el)", max_length = 200, blank = True)
    name_en             = models.CharField("name (en)", max_length = 200, unique = True)
    name_es             = models.CharField("name (es)", max_length = 200, blank = True)
    name_es_AR          = models.CharField("name (es_AR)", max_length = 200, blank = True)
    name_et             = models.CharField("name (et)", max_length = 200, blank = True)
    name_eu             = models.CharField("name (eu)", max_length = 200, blank = True)
    name_fa             = models.CharField("name (fa)", max_length = 200, blank = True)
    name_fi             = models.CharField("name (fi)", max_length = 200, blank = True)
    name_fr             = models.CharField("name (fr)", max_length = 200, blank = True)
    name_ga             = models.CharField("name (ga)", max_length = 200, blank = True)
    name_gl             = models.CharField("name (gl)", max_length = 200, blank = True)
    name_he             = models.CharField("name (he)", max_length = 200, blank = True)
    name_hi             = models.CharField("name (hi)", max_length = 200, blank = True)
    name_hr             = models.CharField("name (hr)", max_length = 200, blank = True)
    name_hu             = models.CharField("name (hu)", max_length = 200, blank = True)
    name_is             = models.CharField("name (is)", max_length = 200, blank = True)
    name_it             = models.CharField("name (it)", max_length = 200, blank = True)
    name_ja             = models.CharField("name (ja)", max_length = 200, blank = True)
    name_ka             = models.CharField("name (ka)", max_length = 200, blank = True)
    name_km             = models.CharField("name (km)", max_length = 200, blank = True)
    name_kn             = models.CharField("name (kn)", max_length = 200, blank = True)
    name_ko             = models.CharField("name (ko)", max_length = 200, blank = True)
    name_lt             = models.CharField("name (lt)", max_length = 200, blank = True)
    name_lv             = models.CharField("name (lv)", max_length = 200, blank = True)
    name_mk             = models.CharField("name (mk)", max_length = 200, blank = True)
    name_nl             = models.CharField("name (nl)", max_length = 200, blank = True)
    name_no             = models.CharField("name (no)", max_length = 200, blank = True)
    name_pl             = models.CharField("name (pl)", max_length = 200, blank = True)
    name_pt             = models.CharField("name (pt)", max_length = 200, blank = True)
    name_pt_BR          = models.CharField("name (pt_BR)", max_length = 200, blank = True)
    name_ro             = models.CharField("name (ro)", max_length = 200, blank = True)
    name_ru             = models.CharField("name (ru)", max_length = 200, blank = True)
    name_sk             = models.CharField("name (sk)", max_length = 200, blank = True)
    name_sl             = models.CharField("name (sl)", max_length = 200, blank = True)
    name_sr             = models.CharField("name (sr)", max_length = 200, blank = True)
    name_sr_Latn        = models.CharField("name (sr_Latn)", max_length = 200, blank = True)
    name_sv             = models.CharField("name (sv)", max_length = 200, blank = True)
    name_ta             = models.CharField("name (ta)", max_length = 200, blank = True)
    name_te             = models.CharField("name (te)", max_length = 200, blank = True)
    name_th             = models.CharField("name (th)", max_length = 200, blank = True)
    name_tr             = models.CharField("name (tr)", max_length = 200, blank = True)
    name_uk             = models.CharField("name (uk)", max_length = 200, blank = True)
    name_zh_CN          = models.CharField("name (zh_CN)", max_length = 200, blank = True)
    name_zh_TW          = models.CharField("name (zh_TW)", max_length = 200, blank = True)
    
    slug                = models.SlugField(max_length = 200, unique = True,
                                help_text = "Automatically created from the English name")

    class Meta:
        ordering             = ('name_en',)
        verbose_name         = 'country'
        verbose_name_plural  = 'countries'


    def __unicode__(self):
        try:
            name_field = "name_%s" % translation.get_language()
            value = getattr(self, name_field)
            if value:
                return u'%s' % value
            else:
                return self.name_en
        except:
            return self.name_en


class Language(models.Model):
    """
    Data model of world languages.
    """
    iso_639_2_alpha2    = models.CharField(max_length = 2, unique = True)
    iso_639_2_alpha3    = models.CharField(max_length = 3, unique = True)
    name_ar             = models.CharField("name (ar)", max_length = 200, blank = True)
    name_bg             = models.CharField("name (bg)", max_length = 200, blank = True)
    name_bn             = models.CharField("name (bn)", max_length = 200, blank = True)
    name_ca             = models.CharField("name (ca)", max_length = 200, blank = True)
    name_cs             = models.CharField("name (cs)", max_length = 200, blank = True)
    name_cy             = models.CharField("name (cy)", max_length = 200, blank = True)
    name_da             = models.CharField("name (da)", max_length = 200, blank = True)
    name_de             = models.CharField("name (de)", max_length = 200, blank = True)
    name_el             = models.CharField("name (el)", max_length = 200, blank = True)
    name_en             = models.CharField("name (en)", max_length = 200, unique = True)
    name_es             = models.CharField("name (es)", max_length = 200, blank = True)
    name_es_AR          = models.CharField("name (es_AR)", max_length = 200, blank = True)
    name_et             = models.CharField("name (et)", max_length = 200, blank = True)
    name_eu             = models.CharField("name (eu)", max_length = 200, blank = True)
    name_fa             = models.CharField("name (fa)", max_length = 200, blank = True)
    name_fi             = models.CharField("name (fi)", max_length = 200, blank = True)
    name_fr             = models.CharField("name (fr)", max_length = 200, blank = True)
    name_ga             = models.CharField("name (ga)", max_length = 200, blank = True)
    name_gl             = models.CharField("name (gl)", max_length = 200, blank = True)
    name_he             = models.CharField("name (he)", max_length = 200, blank = True)
    name_hi             = models.CharField("name (hi)", max_length = 200, blank = True)
    name_hr             = models.CharField("name (hr)", max_length = 200, blank = True)
    name_hu             = models.CharField("name (hu)", max_length = 200, blank = True)
    name_is             = models.CharField("name (is)", max_length = 200, blank = True)
    name_it             = models.CharField("name (it)", max_length = 200, blank = True)
    name_ja             = models.CharField("name (ja)", max_length = 200, blank = True)
    name_ka             = models.CharField("name (ka)", max_length = 200, blank = True)
    name_km             = models.CharField("name (km)", max_length = 200, blank = True)
    name_kn             = models.CharField("name (kn)", max_length = 200, blank = True)
    name_ko             = models.CharField("name (ko)", max_length = 200, blank = True)
    name_lt             = models.CharField("name (lt)", max_length = 200, blank = True)
    name_lv             = models.CharField("name (lv)", max_length = 200, blank = True)
    name_mk             = models.CharField("name (mk)", max_length = 200, blank = True)
    name_nl             = models.CharField("name (nl)", max_length = 200, blank = True)
    name_no             = models.CharField("name (no)", max_length = 200, blank = True)
    name_pl             = models.CharField("name (pl)", max_length = 200, blank = True)
    name_pt             = models.CharField("name (pt)", max_length = 200, blank = True)
    name_pt_BR          = models.CharField("name (pt_BR)", max_length = 200, blank = True)
    name_ro             = models.CharField("name (ro)", max_length = 200, blank = True)
    name_ru             = models.CharField("name (ru)", max_length = 200, blank = True)
    name_sk             = models.CharField("name (sk)", max_length = 200, blank = True)
    name_sl             = models.CharField("name (sl)", max_length = 200, blank = True)
    name_sr             = models.CharField("name (sr)", max_length = 200, blank = True)
    name_sr_Latn        = models.CharField("name (sr_Latn)", max_length = 200, blank = True)
    name_sv             = models.CharField("name (sv)", max_length = 200, blank = True)
    name_ta             = models.CharField("name (ta)", max_length = 200, blank = True)
    name_te             = models.CharField("name (te)", max_length = 200, blank = True)
    name_th             = models.CharField("name (th)", max_length = 200, blank = True)
    name_tr             = models.CharField("name (tr)", max_length = 200, blank = True)
    name_uk             = models.CharField("name (uk)", max_length = 200, blank = True)
    name_zh_CN          = models.CharField("name (zh_CN)", max_length = 200, blank = True)
    name_zh_TW          = models.CharField("name (zh_TW)", max_length = 200, blank = True)
    
    comment             = models.CharField("comment", max_length = 200, blank = True)

    class Meta:
        ordering             = ('name_en', )
        verbose_name         = 'language'
        verbose_name_plural  = 'languages'


    def __unicode__(self):
        try:
            name_field = "name_%s" % translation.get_language()
            value = getattr(self, name_field)
            if value:
                return u'%s' % value
            else:
                return self.name_en
        except:
            return self.name_en

