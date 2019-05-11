const ngxWallabyJest = require('ngx-wallaby-jest');

module.exports = (wallaby) => {
    return {
        files: [
            'src/**/*.+(ts|html|json|snap|css|less|sass|scss|jpg|jpeg|gif|png|svg)',
            'tsconfig.json',
            'tsconfig.spec.json',
            'package.json',
            '!projects/**/*.spec.ts',
        ],

        tests: ['src/**/*.spec.ts'],

        env: {
            type: 'node',
            runner: 'node'
        },
        compliers: {
            '**/*.ts?(x)': wallaby.compliers.typescript({ module: 'commonjs'}),
        },
        preprocessors: {
            // This translate templateUrl and styleUrls to the right implementation
            // For wallaby
            'app/**/*.component.ts': ngxWallabyJest,
        },
        testFramework: 'jest'
    }
}