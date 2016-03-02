:title: Clustered Standard Errors in Statsmodel OLS
:authors: Maclean Gaulin
:date: 2016-03-01
:tags: python,statsmodel,pandas,econometrics


I am using Statsmodel_ instead of STATA where possible, and wanted to cluster standard errors by firm.
The statsmodels documentation is a bit unclear, so I figured I'd put up a working excerpt.
The problem I encountered was I use Patsy_ to create the endog/exog matrices, and statsmodel requires the cluster group Series to match length.
(Aside: There's an open Github_ issue about this.)
I'm sure there are more clever solutions, but mine was to give Patsy a dataframe with no missing data.

.. code-block:: python
    :linenos: inline

    # Selection criteria
    select_df = df[(df['at']>1) & (df['ff12']!=8)].sort_values('cik y_q'.split())
    # Columns that appear in regressions, as well as group variable (here CIK)
    cols = 'cik cp ni_at re_at xrd_at at y_q ff12'.split()
    # Final dataframe with no missing data.
    # This gets the patsy arrays and group series to have the same length.
    reg_df = select_df.ix[select_df[cols].notnull().all(axis=1), cols]

    mod = sm.OLS.from_formula('cp ~ ni_at + re_at + xrd_at + np.log(at) '
                              '+ C(y_q) + C(ff12)', reg_df)

    res = mod.fit(cov_type='cluster', cov_kwds={'groups': reg_df['cik']})

    print("\n".join([_ for _ in str(res.summary()).split('\n') if 'C(' not in _]))

.. _Patsy: https://patsy.readthedocs.org/en/latest/
.. _Statsmodel: http://statsmodels.sourceforge.net/devel/generated/statsmodels.regression.linear_model.RegressionResults.get_robustcov_results.html
.. _Github: https://github.com/statsmodels/statsmodels/issues/1220

