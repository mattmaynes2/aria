
function columnify (table) {
    var columns = Object.keys(table[0]),
        widths  = columns.reduce((w, column) => {
            w[column] = 1 + maxLength(table, column);
            return w;
        }, {}),
        spacedColumns = columns.map((column) => {
            var name = column.toString().toUpperCase();
            return name + Array(widths[column] - name.length).join(' ');
        }),
        header = '| ' + spacedColumns.join(' | ') + ' |\n| ' + spacedColumns.map((c) => {
            return Array(1 + c.length).join('-');
        }).join(' | ') + ' |\n';

    return header + table.map((row) => {
        return '| ' + columns.map((column) => {
            var cell = (row[column] || '').toString();
            return cell + Array(widths[column] - cell.length).join(' ');
        }).join(' | ') + ' |';
    }).join('\n');
}

function maxLength (table, column) {
    return Math.max(column.length, table.reduce((m, row) => {
        return Math.max((row[column] || '').toString().length, m);
    }, 0));
}

module.exports = columnify;
