setUserDisplayData: (userData) ->
  if userData
    # set username
    if userData.is_free_trial
      # show upgrade link if free trial plan
    if userData.plan_remaining_days?
      # show remaining days of free trial
      if userData.plan_remaining_days <= 0
        # set one upgradeText
      else
        # set another upgradeText

      $('[data-upgrade-days]').text(upgradeText)
      $('[data-upgrade-days]').show()
