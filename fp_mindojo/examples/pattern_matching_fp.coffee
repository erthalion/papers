setUserDisplayData: (userData) ->
  commonPart = (text) ->
      $('[data-upgrade-days]').text(text)
      $('[data-upgrade-days]').show()
  if userData
    # set username
  else
    return
  if userData.is_free_trial
      # show upgrade link if free trial plan
  if not userData.plan_remaining_days?
    return
  if userData.plan_remaining_days <= 0
      # set one upgradeText
      commonPart(upgradeText)
  else
      # set another upgradeText
      commonPart(upgradeText)
