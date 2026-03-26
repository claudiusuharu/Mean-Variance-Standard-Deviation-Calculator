import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import seaborn as sns

df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]


def draw_line_plot():
    fig, ax = plt.subplots(figsize=(18, 6))

    ax.plot(df.index, df['value'], color='red', linewidth=0.8)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    df_bar = df.copy()
    df_bar['year']  = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    df_pivot = (
        df_bar
        .groupby(['year', 'month'])['value']
        .mean()
        .unstack()
    )

    month_labels = ['January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November', 'December']
    df_pivot.columns = month_labels

    fig, ax = plt.subplots(figsize=(14, 7))

    df_pivot.plot(kind='bar', ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')

    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year']       = df_box['date'].dt.year
    df_box['month']      = df_box['date'].dt.strftime('%b')
    df_box['month_num']  = df_box['date'].dt.month

    df_box = df_box.sort_values('month_num')

    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    fig, axes = plt.subplots(1, 2, figsize=(20, 7))

    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(data=df_box, x='month', y='value', order=month_order, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    fig.savefig('box_plot.png')
    return fig
