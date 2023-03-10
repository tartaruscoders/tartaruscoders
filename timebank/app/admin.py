# from django.contrib import admin
# from .models import Profile, Request, Contribution, Country, League, LeagueRank

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user', 'idn_or_ssn', 'is_elder', 'is_volunteer', 'location', 'time_credits')
#     search_fields = ('user__username', 'location')

# class RequestAdmin(admin.ModelAdmin):
#     list_display = ('title', 'duration', 'location', 'creator', 'volunteer', 'date_created')
#     search_fields = ('title', 'creator__user__username', 'location')

# class ContributionAdmin(admin.ModelAdmin):
#     list_display = ('amount', 'contributor', 'date_created')
#     search_fields = ('contributor__user__username',)

# class CountryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'platinum_threshold', 'gold_threshold', 'silver_threshold', 'bronze_threshold')
#     search_fields = ('name',)

# class LeagueAdmin(admin.ModelAdmin):
#     list_display = ('name', 'country', 'time_credit_threshold')
#     search_fields = ('name', 'country__name')

# class LeagueRankAdmin(admin.ModelAdmin):
#     list_display = ('league', 'profile', 'rank')
#     search_fields = ('league__name', 'profile__user__username')

# admin.site.register(Profile, ProfileAdmin)
# admin.site.register(Request, RequestAdmin)
# admin.site.register(Contribution, ContributionAdmin)
# admin.site.register(Country, CountryAdmin)
# admin.site.register(League, LeagueAdmin)
# admin.site.register(LeagueRank, LeagueRankAdmin)
